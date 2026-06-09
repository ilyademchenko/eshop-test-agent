---
description: Записать новый сценарий через playwright codegen в recorded_scripts/
argument-hint: <page> <name> [url-path]
---

Запиши новый Playwright-сценарий для eshop.sibur.ru.

Аргументы: `$ARGUMENTS` — это `<page> <name> [url-path]`, где
- `page` — папка-страница (auth, catalog, cart, checkout, ...),
- `name` — имя файла скрипта,
- `url-path` — необязательный начальный путь (например `/catalog`).

Шаги:
1. Запусти `python utils/recorder.py --page <page> --name <name> --url <url-path>`.
   Команда откроет браузер на `settings.BASE_URL + url-path` и сохранит запись в
   `recorded_scripts/<page>/<name>.py`.
2. После записи покажи получившийся файл и кратко опиши записанные действия.
3. НЕ раскладывай по слоям на этом шаге — для этого есть `/scenario-to-test`.

Помни про Siebel-специфику из CLAUDE.md (codegen запишет нестабильные URL и
текстовые локаторы — это нормально, нормализация будет на следующем шаге).
