from playwright.async_api import Page, Locator


class MainPage:
    """Авторизованный личный кабинет eshop.sibur.ru.

    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def mask_overlay(self) -> Locator:
        """Спиннер-маска загрузки Siebel."""
        return self.page.locator("#maskoverlay")

    @property
    def catalog_link(self) -> Locator:
        """Ссылка 'Каталог' в шапке — признак отрисованного кабинета."""
        return self.page.get_by_role("link", name="Каталог").first

    @property
    def profile_icon(self) -> Locator:
        """Иконка профиля (аватар) в правом верхнем углу."""
        return self.page.locator(".sib-ecustomer-login").first

    @property
    def logout_button(self) -> Locator:
        """Кнопка 'Выйти' внутри попапа профиля."""
        return self.page.locator(".profile-popup__exit, .js-exit-profile").first
