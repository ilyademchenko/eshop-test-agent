from playwright.async_api import Page
from .base_page import BasePage


class AuthPage(BasePage):
    """Страница авторизации eshop.sibur.ru"""

    URL = "/login"

    # --- Локаторы ---
    LOGIN_INPUT = "[data-testid='login-input'], input[name='login'], input[type='email']"
    PASSWORD_INPUT = "[data-testid='password-input'], input[name='password'], input[type='password']"
    SUBMIT_BUTTON = "[data-testid='submit-btn'], button[type='submit']"
    ERROR_MESSAGE = "[data-testid='error-message'], .error-message, .alert-error"
    USER_MENU = "[data-testid='user-menu'], .user-menu, .header-user"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    async def open(self) -> "AuthPage":
        await self.navigate(self.URL)
        return self

    async def login(self, login: str, password: str) -> None:
        await self.fill(self.LOGIN_INPUT, login)
        await self.fill(self.PASSWORD_INPUT, password)
        await self.click(self.SUBMIT_BUTTON)
        await self.page.wait_for_load_state("networkidle")

    async def login_as_default_user(self) -> None:
        from config import settings
        await self.login(settings.LOGIN, settings.PASSWORD)

    async def is_logged_in(self) -> bool:
        return await self.is_visible(self.USER_MENU)

    async def get_error_message(self) -> str:
        return await self.get_text(self.ERROR_MESSAGE)
