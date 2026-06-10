"""Запускает сессию Managed Agent для авторинга Playwright-тестов.

Перед первым запуском создайте агента и среду:
    ant beta:agents create < agent/agent.yaml      # сохраните AGENT_ID
    ant beta:environments create < agent/environment.yaml  # сохраните ENV_ID

Затем задайте переменные окружения в .env или экспортируйте вручную:
    AGENT_ID=agent_...
    ENV_ID=env_...
    GITHUB_TOKEN=ghp_...   # PAT с правом Contents: Read and write
    REPO_URL=https://github.com/org/repo  # URL репозитория

Использование:
    python agent/run_session.py "Напиши тест test_logout в tests/e2e/"
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

import anthropic  # noqa: E402 — после dotenv


AGENT_ID = os.environ.get("AGENT_ID", "")
ENV_ID = os.environ.get("ENV_ID", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO_URL = os.environ.get("REPO_URL", "")


def run_session(task: str) -> None:
    if not AGENT_ID:
        sys.exit(
            "AGENT_ID не задан.\n"
            "Создайте агента: ant beta:agents create < agent/agent.yaml\n"
            "Сохраните ID в .env как AGENT_ID=agent_..."
        )
    if not ENV_ID:
        sys.exit(
            "ENV_ID не задан.\n"
            "Создайте среду: ant beta:environments create < agent/environment.yaml\n"
            "Сохраните ID в .env как ENV_ID=env_..."
        )

    client = anthropic.Anthropic()

    resources = []
    if REPO_URL and GITHUB_TOKEN:
        resources.append(
            {
                "type": "github_repository",
                "url": REPO_URL,
                "authorization_token": GITHUB_TOKEN,
                "mount_path": "/workspace",
                "checkout": {"type": "branch", "name": "main"},
            }
        )

    session = client.beta.sessions.create(
        agent=AGENT_ID,
        environment_id=ENV_ID,
        title=f"test-author: {task[:80]}",
        resources=resources,
    )
    print(f"Сессия: https://platform.claude.com/workspaces/default/sessions/{session.id}\n")

    with client.beta.sessions.events.stream(session_id=session.id) as stream:
        client.beta.sessions.events.send(
            session_id=session.id,
            events=[
                {
                    "type": "user.message",
                    "content": [{"type": "text", "text": task}],
                }
            ],
        )
        for event in stream:
            if event.type == "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="", flush=True)
            elif event.type == "session.status_idle":
                stop = getattr(event, "stop_reason", None)
                if not stop or getattr(stop, "type", None) != "requires_action":
                    break
            elif event.type == "session.status_terminated":
                break

    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python agent/run_session.py '<задача>'")
        print()
        print("Примеры:")
        print("  python agent/run_session.py 'Напиши тест test_logout'")
        print("  python agent/run_session.py 'Почини падающий test_add_to_cart'")
        sys.exit(1)

    run_session(" ".join(sys.argv[1:]))
