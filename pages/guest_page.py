from playwright.async_api import Page, Locator


class GuestPage:
    """Гостевая (неавторизованная) посадочная страница eshop.sibur.ru.

    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def enter_link(self) -> Locator:
        """Ссылка 'Войти' в шапке."""
        return self.page.get_by_role("link", name="Войти")
