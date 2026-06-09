---
description: Создать новый PageObject (только локаторы) по конвенциям проекта
argument-hint: <PageName> [url-or-description]
---

Создай новый PageObject для `$ARGUMENTS`.

Правила (см. CLAUDE.md, слой pages/):
- Файл `pages/<snake_case>.py`, класс `<PascalCase>`.
- Конструктор `__init__(self, page: Page)` сохраняет `self.page`.
- Каждый элемент — `@property`, возвращающий `Locator`. Докстрока на русском.
- ТОЛЬКО локаторы. Никаких `click`/`fill`/`wait`/`expect`/навигации.
- Предпочитай устойчивые селекторы: `get_by_role`, стабильные CSS-классы Siebel
  (`.sib-ecustomer-*`). Избегай локаторов по длинному тексту и сессионным id.
- Зарегистрируй класс в `pages/__init__.py` (импорт + `__all__`).

Если реальные селекторы неизвестны — предупреди и предложи записать сценарий
(`/record-scenario`) или снять DOM временным debug-скриптом.
