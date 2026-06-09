import pytest
from playwright.async_api import Page

from steps import AuthSteps, CatalogSteps
from test_data import get_product_code

PRODUCT_CODE = get_product_code("766583")


@pytest.mark.asyncio
class TestAddToCartViaSearch:
    """Сценарий: пользователь авторизуется, находит продукт через поиск и добавляет его в корзину."""

    async def test_add_product_via_search(self, page: Page):
        auth = AuthSteps(page)
        catalog = CatalogSteps(page)

        await auth.login()
        await catalog.open_catalog()
        product = await catalog.search_product(PRODUCT_CODE)
        await catalog.add_to_cart_from_details()
        await catalog.open_cart()
        await catalog.assert_product_in_cart(product)
