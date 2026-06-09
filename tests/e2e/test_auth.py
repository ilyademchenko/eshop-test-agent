import pytest
from playwright.async_api import Page, expect
from pages import AuthPage


@pytest.mark.asyncio
class TestAuth:
    async def test_login_page_opens(self, page: Page):
        auth = AuthPage(page)
        await auth.open()
        assert "sibur" in (await auth.get_title()).lower() or await auth.is_visible(auth.LOGIN_INPUT)

    async def test_login_with_valid_credentials(self, page: Page):
        auth = AuthPage(page)
        await auth.open()
        await auth.login_as_default_user()
        assert await auth.is_logged_in(), "Пользователь не авторизован после входа"

    async def test_login_with_invalid_credentials(self, page: Page):
        auth = AuthPage(page)
        await auth.open()
        await auth.login("wrong@example.com", "wrongpassword")
        assert await auth.is_visible(auth.ERROR_MESSAGE), "Ошибка авторизации не показана"
