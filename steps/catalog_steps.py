from dataclasses import dataclass, field
from playwright.async_api import Page, expect

from config import settings
from pages import MainPage, CatalogPage, ProductDetailsPage, CartPage

expect.set_options(timeout=settings.NAVIGATION_TIMEOUT)


@dataclass
class ProductInfo:
    """Свойства продукта, собранные со страницы деталей.

    Используется для передачи данных между шагами (например, от страницы
    деталей к проверке корзины).
    """

    code: str
    title: str = field(default="")


class CatalogSteps:
    """Шаги сценария: каталог → поиск продукта → добавление в корзину → проверка."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.main_page = MainPage(page)
        self.catalog_page = CatalogPage(page)
        self.product_details_page = ProductDetailsPage(page)
        self.cart_page = CartPage(page)
        self.page.set_default_timeout(settings.NAVIGATION_TIMEOUT)

    async def wait_spinner_gone(self) -> None:
        """Ждёт исчезновения спиннера-маски Siebel (если он есть)."""
        try:
            await self.main_page.mask_overlay.wait_for(
                state="hidden", timeout=settings.NAVIGATION_TIMEOUT
            )
        except Exception:
            pass

    async def open_catalog(self) -> None:
        """Перейти в каталог через ссылку в шапке и дождаться его загрузки."""
        await self.wait_spinner_gone()
        await expect(self.main_page.catalog_link).to_be_visible()
        await self.main_page.catalog_link.click(no_wait_after=True)
        await self.wait_spinner_gone()
        await expect(self.catalog_page.content_section).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )

    async def search_product(self, product_code: str) -> ProductInfo:
        """Найти продукт по коду через поисковую строку каталога.

        При уникальном коде Siebel сразу переходит на страницу деталей продукта.
        Возвращает ProductInfo с заполненным title, прочитанным со страницы деталей.
        """
        await self.wait_spinner_gone()
        await expect(self.catalog_page.search_input).to_be_visible()
        await self.catalog_page.search_input.fill(product_code)
        await self.catalog_page.search_input.press("Enter")
        await self.wait_spinner_gone()
        await expect(self.product_details_page.content_section).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )
        title = (await self.product_details_page.product_title.inner_text()).strip()
        return ProductInfo(code=product_code, title=title)

    async def add_to_cart_from_details(self) -> None:
        """Нажать кнопку 'Купить' на странице деталей продукта."""
        await self.wait_spinner_gone()
        await expect(self.product_details_page.add_to_cart_button).to_be_visible()
        await self.product_details_page.add_to_cart_button.click(no_wait_after=True)
        await self.wait_spinner_gone()

    async def open_cart(self) -> None:
        """Открыть корзину через иконку в шапке и дождаться содержимого."""
        await self.wait_spinner_gone()
        await expect(self.main_page.cart_link).to_be_visible()
        await self.main_page.cart_link.click(no_wait_after=True)
        await self.wait_spinner_gone()
        await expect(self.cart_page.content_section).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )

    async def assert_product_in_cart(self, product: ProductInfo) -> None:
        """Проверить, что корзина содержит товар с названием из product.title."""
        await expect(self.cart_page.cart_step).to_be_visible()
        item = self.cart_page.cart_items.filter(has_text=product.title)
        await expect(item).to_be_visible()
