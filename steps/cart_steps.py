from playwright.async_api import Page, expect

from config import settings
from pages import MainPage, ProductListPage

expect.set_options(timeout=settings.NAVIGATION_TIMEOUT)


class CartSteps:
    """Шаги сценария добавления продукта в корзину через Экспресс-покупку."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.main_page = MainPage(page)
        self.product_list_page = ProductListPage(page)
        self.page.set_default_timeout(settings.NAVIGATION_TIMEOUT)

    async def wait_spinner_gone(self) -> None:
        """Ждёт исчезновения спиннера-маски Siebel (если он есть)."""
        try:
            await self.main_page.mask_overlay.wait_for(
                state="hidden", timeout=settings.NAVIGATION_TIMEOUT
            )
        except Exception:
            pass

    async def open_express_buying(self) -> None:
        """Перейти на страницу Экспресс-покупка через вторичное меню."""
        await self.wait_spinner_gone()
        await expect(self.main_page.express_purchase_link).to_be_visible()
        await self.main_page.express_purchase_link.click(no_wait_after=True)
        await self.wait_spinner_gone()
        await expect(self.product_list_page.content_section).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )

    async def add_to_cart_by_code(self, product_code: str) -> None:
        """Найти карточку продукта по коду и нажать 'Купить'.

        Ищет карточку, содержащую product_code в своём тексте.
        Перед кликом ждёт исчезновения спиннера.
        """
        await self.wait_spinner_gone()
        card = self.product_list_page.product_cards.filter(has_text=product_code)
        await expect(card).to_be_visible()
        buy_btn = card.locator(".siebui-icon-addtocartexpress")
        await expect(buy_btn).to_be_visible()
        await buy_btn.click(no_wait_after=True)
        await self.wait_spinner_gone()

    async def assert_product_added(self) -> None:
        """Проверить успешное добавление: страница не упала, корзина доступна."""
        await expect(self.product_list_page.content_section).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )
        await expect(self.main_page.cart_link).to_be_visible()
