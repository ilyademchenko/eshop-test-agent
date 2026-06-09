import pytest
from playwright.async_api import Page

from steps import AuthSteps


@pytest.mark.asyncio
class TestAuthLogin:
    """Сценарий входа и выхода. Тест обращается только к шагам (steps)."""

    async def test_login_and_logout(self, page: Page):
        steps = AuthSteps(page)

        # Вход
        await steps.open_site()
        await steps.go_to_login_form()
        await steps.fill_credentials_from_settings()
        await steps.accept_checkboxes_if_present()
        await steps.submit_login()
        await steps.assert_logged_in()

        # Выход
        await steps.logout()
        await steps.assert_logged_out()
