import pytest
from playwright.async_api import Page

from steps import AuthSteps, CartSteps
from test_data import get_product_code

PRODUCT_CODE = get_product_code("766583")


@pytest.mark.asyncio
class TestAddToCart:
    """Сценарий: авторизованный пользователь добавляет продукт в корзину."""

    async def test_add_product_to_cart(self, authenticated_page: Page):
        steps = CartSteps(authenticated_page)

        await steps.open_express_buying()
        await steps.add_to_cart_by_code(PRODUCT_CODE)
        await steps.assert_product_added()
