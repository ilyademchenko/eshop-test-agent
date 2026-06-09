from playwright.async_api import Page, Locator


class LoginPage:
    """Страница формы авторизации Siebel (SWECmd=Start).

    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def login_input(self) -> Locator:
        return self.page.get_by_role("textbox", name="Логин")

    @property
    def password_input(self) -> Locator:
        return self.page.get_by_role("textbox", name="Пароль")

    @property
    def captcha_checkbox(self) -> Locator:
        """Чекбокс 'Я не робот' (появляется не всегда)."""
        return self.page.get_by_role("checkbox", name="Я не робот")

    @property
    def consent_checkbox(self) -> Locator:
        """Чекбокс согласия на обработку персональных данных (появляется не всегда)."""
        return self.page.get_by_role("checkbox", name="Я даю согласие на обработку")

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Вход")
