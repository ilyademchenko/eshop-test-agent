# Архитектура проекта

E2E-автотесты eshop.sibur.ru на Playwright (async) с паттерном Page Object Model
и разделением на слои.

## Слои и поток зависимостей

```
┌─────────────┐
│   tests/    │  Сценарии. Вызывают только шаги.
└──────┬──────┘
       │ использует
┌──────▼──────┐      ┌──────────────┐
│   steps/    │─────▶│  test_data/  │  Данные по алиасам (пользователи, payload).
│             │      └──────────────┘
│ действия,   │      ┌──────────────┐
│ ожидания,   │─────▶│   config/    │  settings.py + .env (BASE_URL, секреты, таймауты).
│ проверки    │      └──────────────┘
└──────┬──────┘
       │ использует
┌──────▼──────┐
│   pages/    │  Только локаторы (@property → Locator).
└─────────────┘

fixtures/   — pytest-фикстуры browser/context/page (function-scoped).
utils/      — recorder.py (обёртка playwright codegen), script_converter.py.
recorded_scripts/<page>/ — сырые записи codegen.
```

Зависимости идут строго сверху вниз. Слой не знает о вышестоящих.

## Ответственность слоёв

| Слой | Что можно | Что нельзя |
|------|-----------|------------|
| `tests/` | Вызовы методов `*Steps` | Локаторы, `page` API, `settings`, `test_data` |
| `steps/` | Действия, ожидания, `expect`, оркестрация | Хранить селекторы (берёт их из pages) |
| `pages/` | `@property` → `Locator` | Любые действия, ожидания, `expect` |
| `test_data/` | dataclass'ы, реестры по алиасам | Логику работы с UI |
| `config/` | Чтение `.env`, константы | Бизнес-логику тестов |

## Пример: сценарий входа/выхода

- `pages/guest_page.py` — `enter_link` («Войти»).
- `pages/login_page.py` — поля логина/пароля, чекбоксы, кнопка «Вход».
- `pages/main_page.py` — `mask_overlay`, `catalog_link`, `profile_icon`, `logout_button`.
- `steps/auth_steps.py` — `open_site`, `go_to_login_form`, `fill_credentials_from_settings`,
  `accept_checkboxes_if_present`, `submit_login`, `assert_logged_in`, `logout`,
  `assert_logged_out`, `login` (композит).
- `test_data/users.py` — `USERS["КЗДТ"]`.
- `tests/e2e/test_auth_login.py` — только вызовы шагов.

## Агентная разработка

- `CLAUDE.md` — правила и Siebel-специфика для AI-агента.
- `.claude/commands/` — слэш-команды: `/record-scenario`, `/scenario-to-test`,
  `/add-page`, `/scan-page`, `/run-tests`.
- `.claude/agents/test-author.md` — субагент для авторинга/починки тестов.

См. `CLAUDE.md` для подробных правил и разбора граблей Siebel.
