import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from playwright.async_api import Playwright, async_playwright
from config import settings

# Siebel: непрерывные фоновые XHR делают networkidle недостижимым.
# Ждём конкретные элементы DOM и исчезновение спиннеров вместо wait_for_load_state.


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=settings.HEADLESS, slow_mo=settings.SLOW_MO)
    context = await browser.new_context()
    page = await context.new_page()
    page.set_default_timeout(settings.NAVIGATION_TIMEOUT)

    # --- Открываем стартовую страницу и переходим к форме входа ---
    await page.goto(settings.BASE_URL, wait_until="load", timeout=settings.NAVIGATION_TIMEOUT)
    # Клик "Войти" инициирует медленную навигацию Siebel — не ждём её авто-завершения
    await page.get_by_role("link", name="Войти").click(no_wait_after=True)

    # --- Заполняем форму логина ---
    login_field = page.get_by_role("textbox", name="Логин")
    await login_field.wait_for(state="visible")
    await login_field.fill(settings.LOGIN)
    await page.get_by_role("textbox", name="Пароль").fill(settings.PASSWORD)

    # Чекбоксы появляются не всегда
    captcha = page.get_by_role("checkbox", name="Я не робот")
    if await captcha.is_visible():
        await captcha.check()
    consent = page.get_by_role("checkbox", name="Я даю согласие на обработку")
    if await consent.is_visible():
        await consent.check()

    await page.get_by_role("button", name="Вход").click(no_wait_after=True)

    # --- Ждём завершения входа ---
    # Форма логина исчезает
    await login_field.wait_for(state="hidden", timeout=settings.NAVIGATION_TIMEOUT)
    # Маска-оверлей Siebel скрывается
    await _wait_spinner_gone(page)
    # Шапка авторизованного кабинета отрисована
    await page.get_by_role("link", name="Каталог").first.wait_for(
        state="visible", timeout=settings.NAVIGATION_TIMEOUT
    )
    print("OK: авторизация успешна")

    # --- Выход по клику: иконка профиля -> кнопка "Выйти" в попапе ---
    await _wait_spinner_gone(page)
    profile_icon = page.locator(".sib-ecustomer-login").first
    await profile_icon.wait_for(state="visible", timeout=settings.NAVIGATION_TIMEOUT)
    await profile_icon.click()

    logout_btn = page.locator(".profile-popup__exit, .js-exit-profile").first
    await logout_btn.wait_for(state="visible", timeout=settings.NAVIGATION_TIMEOUT)
    await logout_btn.click(no_wait_after=True)

    # Признак успешного выхода: иконка профиля пропала (Siebel уводит на SWECmd=Start)
    await profile_icon.wait_for(state="hidden", timeout=settings.NAVIGATION_TIMEOUT)
    print("OK: выход выполнен")

    await context.close()
    await browser.close()


async def _wait_spinner_gone(page) -> None:
    """Ждёт исчезновения спиннера-маски Siebel (если он есть)."""
    try:
        await page.locator("#maskoverlay").wait_for(state="hidden", timeout=settings.NAVIGATION_TIMEOUT)
    except Exception:
        pass  # маска могла уже исчезнуть или отсутствовать


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
