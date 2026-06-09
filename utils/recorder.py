"""
Обёртка над playwright codegen для записи скриптов в нужную папку.

Использование:
    python utils/recorder.py --page auth --name login
    python utils/recorder.py --page catalog --name search_product
"""

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import settings


def record(page_name: str, script_name: str, url: str = "") -> None:
    output_dir = settings.RECORDED_SCRIPTS_DIR / page_name
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{script_name}.py"
    start_url = f"{settings.BASE_URL}{url}"

    print(f"Запуск playwright codegen → {output_file}")
    print(f"URL: {start_url}")
    print("Запишите действия в браузере, затем закройте окно кодогенератора.\n")

    cmd = [
        sys.executable, "-m", "playwright", "codegen",
        "--target", "python-async",
        "--output", str(output_file),
        start_url,
    ]

    subprocess.run(cmd, check=True)
    print(f"\nСкрипт сохранён: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Запись Playwright скрипта")
    parser.add_argument("--page", required=True, help="Имя папки (auth, catalog, cart, ...)")
    parser.add_argument("--name", required=True, help="Имя файла скрипта")
    parser.add_argument("--url", default="", help="Начальный URL-путь (например /catalog)")
    args = parser.parse_args()

    record(args.page, args.name, args.url)


if __name__ == "__main__":
    main()
