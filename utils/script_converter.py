"""
Утилита для конвертации записанных Playwright-скриптов в методы Page Object.

Использование:
    python utils/script_converter.py recorded_scripts/auth/login.py --page LoginPage
"""

import re
import sys
from pathlib import Path


# Паттерны для замены playwright codegen → POM методы
REPLACEMENTS = [
    # page.goto(url) → await self.navigate(path)
    (
        r'page\.goto\("https://eshop\.sibur\.ru([^"]*?)"\)',
        r'await self.navigate("\1")',
    ),
    # page.fill(selector, value) → await self.fill(selector, value)
    (r"page\.fill\(", "await self.fill("),
    # page.click(selector) → await self.click(selector)
    (r"page\.click\(", "await self.click("),
    # page.locator(selector).fill(value) → await self.fill(selector, value) — упрощение
    (r"await page\.locator\(([^)]+)\)\.fill\(([^)]+)\)", r"await self.fill(\1, \2)"),
    # await page.locator(selector).click() → await self.click(selector)
    (r"await page\.locator\(([^)]+)\)\.click\(\)", r"await self.click(\1)"),
    # page.wait_for_load_state → await self.page.wait_for_load_state
    (r"page\.wait_for_load_state", "await self.page.wait_for_load_state"),
    # expect(page.locator(...)).to_be_visible() → await self.expect_visible(...)
    (
        r'expect\(page\.locator\(([^)]+)\)\)\.to_be_visible\(\)',
        r"await self.expect_visible(\1)",
    ),
]


def convert_script(source: str) -> str:
    result = source
    for pattern, replacement in REPLACEMENTS:
        result = re.sub(pattern, replacement, result)
    return result


def wrap_as_page_method(converted: str, method_name: str) -> str:
    lines = converted.strip().split("\n")
    body = "\n".join(f"        {line}" for line in lines if line.strip())
    return f"    async def {method_name}(self) -> None:\n{body}\n"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Конвертер playwright codegen → POM метод")
    parser.add_argument("script", help="Путь к записанному скрипту")
    parser.add_argument("--method", default="recorded_action", help="Имя метода")
    parser.add_argument("--output", help="Файл для записи (по умолчанию — stdout)")
    args = parser.parse_args()

    source = Path(args.script).read_text(encoding="utf-8")
    converted = convert_script(source)
    wrapped = wrap_as_page_method(converted, args.method)

    if args.output:
        Path(args.output).write_text(wrapped, encoding="utf-8")
        print(f"Записано в {args.output}")
    else:
        print(wrapped)


if __name__ == "__main__":
    main()
