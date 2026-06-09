from playwright.async_api import Page
from .base_page import BasePage


class CatalogPage(BasePage):
    """Страница каталога продуктов eshop.sibur.ru"""

    URL = "/catalog"

    # --- Локаторы ---
    SEARCH_INPUT = "[data-testid='search-input'], input[placeholder*='Поиск'], input[name='search']"
    SEARCH_BUTTON = "[data-testid='search-btn'], button[type='submit'][form*='search']"
    PRODUCT_CARD = "[data-testid='product-card'], .product-card, .catalog-item"
    PRODUCT_TITLE = "[data-testid='product-title'], .product-title, .product-name"
    PRODUCT_PRICE = "[data-testid='product-price'], .product-price, .price"
    ADD_TO_CART_BUTTON = "[data-testid='add-to-cart'], .add-to-cart, button:has-text('В корзину')"
    FILTER_PANEL = "[data-testid='filter-panel'], .filter-panel, .filters"
    CATEGORY_LINK = "[data-testid='category-link'], .category-link, .sidebar-category a"
    PAGINATION_NEXT = "[data-testid='pagination-next'], .pagination-next, a[rel='next']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    async def open(self) -> "CatalogPage":
        await self.navigate(self.URL)
        return self

    async def search(self, query: str) -> None:
        await self.fill(self.SEARCH_INPUT, query)
        await self.click(self.SEARCH_BUTTON)
        await self.page.wait_for_load_state("networkidle")

    async def get_product_titles(self) -> list[str]:
        cards = self.page.locator(self.PRODUCT_TITLE)
        return await cards.all_text_contents()

    async def add_first_product_to_cart(self) -> str:
        title = await self.get_text(f"{self.PRODUCT_CARD}:first-child {self.PRODUCT_TITLE}")
        await self.click(f"{self.PRODUCT_CARD}:first-child {self.ADD_TO_CART_BUTTON}")
        await self.page.wait_for_load_state("networkidle")
        return title

    async def click_product(self, index: int = 0) -> None:
        cards = self.page.locator(self.PRODUCT_CARD)
        await cards.nth(index).click()
        await self.page.wait_for_load_state("networkidle")

    async def get_products_count(self) -> int:
        return await self.page.locator(self.PRODUCT_CARD).count()
