from playwright.async_api import Page
from .base_page import BasePage


class CartPage(BasePage):
    """Страница корзины eshop.sibur.ru"""

    URL = "/cart"

    # --- Локаторы ---
    CART_ITEM = "[data-testid='cart-item'], .cart-item, .basket-item"
    ITEM_TITLE = "[data-testid='item-title'], .item-name, .product-name"
    ITEM_PRICE = "[data-testid='item-price'], .item-price, .price"
    ITEM_QUANTITY = "[data-testid='item-quantity'], input[name='quantity'], .quantity-input"
    REMOVE_BUTTON = "[data-testid='remove-item'], .remove-item, button:has-text('Удалить')"
    TOTAL_PRICE = "[data-testid='total-price'], .total-price, .cart-total"
    CHECKOUT_BUTTON = "[data-testid='checkout-btn'], .checkout-btn, a:has-text('Оформить')"
    EMPTY_CART_MESSAGE = "[data-testid='empty-cart'], .empty-cart, :text('Корзина пуста')"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    async def open(self) -> "CartPage":
        await self.navigate(self.URL)
        return self

    async def get_items_count(self) -> int:
        return await self.page.locator(self.CART_ITEM).count()

    async def get_total_price(self) -> str:
        return await self.get_text(self.TOTAL_PRICE)

    async def remove_item(self, index: int = 0) -> None:
        buttons = self.page.locator(self.REMOVE_BUTTON)
        await buttons.nth(index).click()
        await self.page.wait_for_load_state("networkidle")

    async def set_item_quantity(self, quantity: int, index: int = 0) -> None:
        inputs = self.page.locator(self.ITEM_QUANTITY)
        await inputs.nth(index).fill(str(quantity))
        await inputs.nth(index).press("Enter")
        await self.page.wait_for_load_state("networkidle")

    async def proceed_to_checkout(self) -> None:
        await self.click(self.CHECKOUT_BUTTON)
        await self.page.wait_for_load_state("networkidle")

    async def is_empty(self) -> bool:
        return await self.is_visible(self.EMPTY_CART_MESSAGE)
