from playwright.async_api import Page, Locator


class CartPage:
    """Страница оформления заказа (корзина) eshop.sibur.ru.

    Открывается по клику на иконку корзины (.sib-ecustomer-header-link-cart-info).
    Siebel рендерит содержимое корзины поверх текущего view (overlay).
    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Секции страницы ---

    @property
    def content_section(self) -> Locator:
        """Основной контейнер страницы оформления заказа."""
        return self.page.locator(".checkout")

    @property
    def header(self) -> Locator:
        """Заголовок страницы 'Оформление заказа'."""
        return self.page.locator(".checkout__header")

    @property
    def cart_step(self) -> Locator:
        """Первый шаг оформления — список товаров в корзине."""
        return self.page.locator(".checkout-step").first

    @property
    def cart_step_title(self) -> Locator:
        """Заголовок шага ('Товары в корзине')."""
        return self.page.locator(".checkout-step__title").first

    @property
    def cart_step_content(self) -> Locator:
        """Содержимое шага — список позиций заказа."""
        return self.page.locator(".checkout-step__content").first

    @property
    def aside_summary(self) -> Locator:
        """Боковая панель с итоговой информацией по заказу."""
        return self.page.locator(".checkout__aside")

    # --- Строки товаров ---

    @property
    def cart_items(self) -> Locator:
        """Коллекция строк товаров в корзине."""
        return self.page.locator(".checkout-element")

    @property
    def cart_item_titles(self) -> Locator:
        """Коллекция названий товаров в корзине."""
        return self.page.locator(".checkout-product__title")

    @property
    def cart_item_prices(self) -> Locator:
        """Коллекция цен товаров (числовые значения)."""
        return self.page.locator(".checkout-product__price-value")

    # --- Кнопки управления ---

    @property
    def delete_all_button(self) -> Locator:
        """Кнопка 'Удалить все' — очистить корзину."""
        return self.page.locator(".siebui-icon-sibcartdeleteall")

    @property
    def next_step_button(self) -> Locator:
        """Кнопка 'Далее' — перейти к следующему шагу оформления."""
        return self.page.locator(".checkout-step__next")
