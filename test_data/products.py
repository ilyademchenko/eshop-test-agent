"""Тестовые данные: продукты для добавления в корзину."""

PRODUCTS: dict[str, str] = {
    "766583": "766583",
}


def get_product_code(alias: str) -> str:
    """Вернуть код продукта по алиасу."""
    try:
        return PRODUCTS[alias]
    except KeyError:
        raise KeyError(
            f"Продукт с алиасом '{alias}' не найден. Доступные: {list(PRODUCTS)}"
        )
