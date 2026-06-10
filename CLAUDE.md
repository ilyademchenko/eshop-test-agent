# CLAUDE.md

Гайд для AI-агента по проекту автотестов **eshop.sibur.ru** (Playwright + Page Object Model).

## Назначение

E2E-автотесты на Python/Playwright (async) для Siebel-портала eshop.sibur.ru.
Сценарии записываются через `playwright codegen`, затем раскладываются по слоям.

## Архитектура слоёв

Зависимости строго в одну сторону: `tests → steps → pages`, данные — в `test_data`.

```
tests/        Только вызовы шагов. Ни локаторов, ни settings, ни Playwright API.
steps/        Действия, ожидания, проверки (expect). Оркестрирует pages + test_data.
pages/        ТОЛЬКО локаторы (@property → Locator). Никаких действий и ожиданий.
test_data/    Тестовые данные: пользователи по алиасам, payload'ы.
config/        Настройки (settings.py) + секреты из .env.
fixtures/      Pytest-фикстуры (browser, context, page, authenticated_page).
recorded_scripts/  Сырые записи playwright codegen, по папкам = страницам.
utils/         recorder.py (обёртка codegen), script_converter.py.
```

### Правила по слоям

- **pages/** — класс на страницу, каждый локатор — `@property`, возвращающий `Locator`.
  Никаких `click`/`fill`/`wait`/`expect` внутри. Только описание элементов.
  **Одна Siebel view = один файл = один класс.** Каждая отдельная страница (view) —
  отдельный `*Page`-класс в своём файле, зарегистрированный в `pages/__init__.py`.
  Проверяй при создании: если Siebel URL меняет `SWEView=` — это новая страница,
  нужен отдельный PageObject.
- **steps/** — класс `*Steps`, принимает `page`, инстанцирует нужные PageObject.
  Здесь живут все действия, ожидания и `expect`-проверки. Методы — атомарные шаги
  плюс при необходимости композитные (`login`).
  **Принцип принадлежности шага:** метод принадлежит тому `*Steps`-классу, чей PageObject
  активен в момент **начала** шага — то есть описывает страницу, на которой находится
  пользователь, когда шаг запускается. Навигационный шаг, который уводит пользователя
  на другую страницу, принадлежит Steps-классу страницы **отправления**, а не назначения.
  Пример: `open_cart` запускается со страницы деталей продукта → живёт в `CatalogSteps`,
  хотя внутри проверяет `cart_page.content_section`. `CartSteps` начинается только тогда,
  когда пользователь уже находится внутри корзины.
- **tests/** — обращается ИСКЛЮЧИТЕЛЬНО к методам `*Steps`. Никакого прямого доступа
  к локаторам, `page`, `settings` или `test_data`.
- **test_data/** — реестры по алиасам (`USERS["КЗДТ"]`). Логин в данных, пароль из `.env`.

## Siebel-специфика (важные грабли)

Портал на Oracle Siebel Open UI — поведение нетипичное, эти правила обязательны:

1. **`networkidle` недостижим** — Siebel шлёт фоновые XHR непрерывно.
   НИКОГДА не используй `wait_for_load_state("networkidle")`.
   Жди конкретные элементы DOM (`expect(locator).to_be_visible()`).
2. **Спиннер-маска `#maskoverlay`** перекрывает страницу после действий.
   Перед кликами в кабинете жди `mask_overlay` в состоянии `hidden`.
3. **Медленная навигация** — клики «Войти»/«Вход»/«Выйти» запускают долгие редиректы.
   Используй `.click(no_wait_after=True)` и затем жди следующий элемент.
4. **`expect` имеет собственный таймаут 5с**, не зависящий от `page.set_default_timeout`.
   В steps вызывается `expect.set_options(timeout=settings.NAVIGATION_TIMEOUT)`.
5. **Выход** — по клику: иконка профиля `.sib-ecustomer-login` → попап → `.profile-popup__exit`.
   Признак успешного выхода — исчезновение иконки профиля (Siebel уводит на `SWECmd=Start`).
6. **Капча/согласие** (`Я не робот`, `Я даю согласие...`) появляются не всегда —
   проверяй `is_visible()` перед `check()`.

## Pytest-фикстуры

- Все async-фикстуры **function-scoped**. session-scoped async-фикстура при
  function-scoped event loop в pytest-asyncio даёт дедлок — не делай session-scope.
- `asyncio_mode = auto` (в pyproject.toml) — `async def test_*` работают без декоратора,
  но в проекте принято явно ставить `@pytest.mark.asyncio` на классах.

## Рабочий процесс: запись → тест

Готовые слэш-команды в `.claude/commands/`: `/record-scenario`, `/scenario-to-test`,
`/add-page`, `/scan-page` (прочитать страницу и наполнить PageObject локаторами),
`/run-tests`. Кратко:

1. `python utils/recorder.py --page <page> --name <name> --url <path>` — записать.
2. Прогнать запись (`python recorded_scripts/<page>/<name>.py`), найти реальные селекторы
   (при необходимости — временный debug-скрипт со скриншотом/дампом DOM, удалить после).
3. Разложить по слоям: локаторы → `pages/`, действия/ожидания/проверки → `steps/`,
   вызовы шагов → `tests/`, данные → `test_data/`.
4. Запустить тест, починить под Siebel-специфику.

## Запуск

```bash
pip install -r requirements.txt && playwright install chromium   # установка
python -m pytest tests/e2e/test_auth_login.py -v -s              # один тест
python -m pytest tests/ -v                                       # все
```

Конфигурация — через `.env` (см. `.env.example`). `HEADLESS=false` для отладки.

## Стиль кода

- Async/await везде (Playwright async API).
- Русские докстроки и комментарии — как в существующем коде.
- `ruff` + `black`, line-length 100 (см. pyproject.toml).
- Имена методов-шагов — глагол: `open_site`, `fill_credentials`, `assert_logged_in`.
