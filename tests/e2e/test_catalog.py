import pytest
from playwright.async_api import Page
from pages import CatalogPage


@pytest.mark.asyncio
class TestCatalog:
    async def test_catalog_opens(self, authenticated_page: Page):
        catalog = CatalogPage(authenticated_page)
        await catalog.open()
        count = await catalog.get_products_count()
        assert count > 0, "Каталог пуст — товары не загружены"

    async def test_search_returns_results(self, authenticated_page: Page):
        catalog = CatalogPage(authenticated_page)
        await catalog.open()
        await catalog.search("полиэтилен")
        count = await catalog.get_products_count()
        assert count > 0, "Поиск не вернул результатов"

    async def test_add_product_to_cart(self, authenticated_page: Page):
        catalog = CatalogPage(authenticated_page)
        await catalog.open()
        title = await catalog.add_first_product_to_cart()
        assert title, "Не удалось получить название товара"
