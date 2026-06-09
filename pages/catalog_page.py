from playwright.async_api import Page, Locator


class CatalogPage:
    """Страница каталога продуктов eshop.sibur.ru
    (Siebel view: SIB ECOM Product Catalog View).

    Содержит только локаторы. Действия и ожидания — в steps/.
    Общая шапка/меню/подвал не дублируются — они описаны в MainPage.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Секции страницы ---

    @property
    def catalog_title(self) -> Locator:
        """Заголовок страницы 'Каталог'."""
        return self.page.locator(".catalog-header")

    @property
    def content_section(self) -> Locator:
        """Основная область каталога (сайдбар категорий + контент)."""
        return self.page.locator(".sib-ecom-catalog-view-content")

    @property
    def category_list_section(self) -> Locator:
        """Левый сайдбар со списком категорий (классов продуктов)."""
        return self.page.locator(".sib-ecom-catalog-list")

    @property
    def category_details_section(self) -> Locator:
        """Правая область с содержимым выбранной категории."""
        return self.page.locator(".sib-ecom-catalog-view-content__catalog-categories")

    @property
    def express_banner_section(self) -> Locator:
        """Баннер раздела 'Экспресс-покупка'."""
        return self.page.locator(".express-banner")

    # --- Интерактивные элементы ---

    @property
    def category_tiles(self) -> Locator:
        """Коллекция плиток категорий в левом сайдбаре (для выбора класса продукта)."""
        return self.category_list_section.locator(".siebui-tile")

    @property
    def selected_category_link(self) -> Locator:
        """Ссылка-заголовок выбранной категории в правой области."""
        return self.category_details_section.locator(".category-link")

    @property
    def search_input(self) -> Locator:
        """Поле поиска продукта по каталогу."""
        return self.page.locator("#sib-product-search-input")

    @property
    def learn_more_button(self) -> Locator:
        """Кнопка 'Узнать подробнее' в баннере экспресс-покупки."""
        return self.page.locator(".express-banner__button button")

    @property
    def watch_products_button(self) -> Locator:
        """Кнопка 'Посмотреть продукты' — переход к списку товаров категории."""
        return self.page.locator(".watch-products.js-to-products")

    # --- Всплывающие баннеры ---

    @property
    def cookie_accept_button(self) -> Locator:
        """Кнопка принятия cookie."""
        return self.page.locator(".js-accept-cookie")

    @property
    def site_switch_accept_button(self) -> Locator:
        """Кнопка подтверждения в баннере смены домена (frog-popup)."""
        return self.page.locator(".js-accept-frog")
