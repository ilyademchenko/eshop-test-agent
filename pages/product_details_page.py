from playwright.async_api import Page, Locator


class ProductDetailsPage:
    """Страница карточки продукта eshop.sibur.ru
    (Siebel view: SIB ECOM Product Details View).

    Открывается при поиске по уникальному коду продукта.
    Содержит только локаторы. Действия и ожидания — в steps/.
    Шапка, меню и подвал не дублируются — они описаны в MainPage.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Секции страницы ---

    @property
    def content_section(self) -> Locator:
        """Основной контейнер страницы деталей продукта."""
        return self.page.locator(".sib-ecom-product-details-view")

    @property
    def product_section(self) -> Locator:
        """Блок с основной информацией и действиями по продукту."""
        return self.page.locator(".sib-ecom-product")

    @property
    def product_image(self) -> Locator:
        """Область изображения продукта."""
        return self.page.locator(".sib-ecom-product-img")

    @property
    def product_info_section(self) -> Locator:
        """Блок с названием, ID и кнопками действий."""
        return self.page.locator(".sib-ecom-product-info")

    @property
    def product_price_section(self) -> Locator:
        """Блок с ценой продукта."""
        return self.page.locator(".sib-ecom-product-price")

    @property
    def product_characteristics_section(self) -> Locator:
        """Блок характеристик продукта (технические параметры)."""
        return self.page.locator(".sib-ecom-product-characteristics")

    @property
    def product_attachments_section(self) -> Locator:
        """Блок вложений/документов продукта."""
        return self.page.locator(".sib-ecom-product-attachments")

    # --- Информация о продукте ---

    @property
    def product_title(self) -> Locator:
        """Название продукта (h3)."""
        return self.product_info_section.locator(".sib-ecom-h3")

    @property
    def product_id_text(self) -> Locator:
        """Блок с ID продукта ('ID товара: ...')."""
        return self.product_info_section.locator(".sib-ecom-text--medium")

    # --- Кнопки действий ---

    @property
    def add_to_cart_button(self) -> Locator:
        """Кнопка 'Купить' — добавить продукт в корзину."""
        return self.page.locator(".siebui-icon-addtocartcustom")

    @property
    def add_to_favorites_button(self) -> Locator:
        """Кнопка 'Добавить в избранное'."""
        return self.page.locator(".siebui-icon-sibaddfavorites")

    @property
    def compare_button(self) -> Locator:
        """Кнопка 'Добавить к сравнению'."""
        return self.page.locator(".siebui-icon-sibcompareproduct")

    @property
    def find_analog_button(self) -> Locator:
        """Кнопка 'Найти аналог'."""
        return self.page.locator(".siebui-icon-findanalog")
