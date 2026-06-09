from .base_page import BasePage
from .guest_page import GuestPage
from .login_page import LoginPage
from .main_page import MainPage

# Старые черновые PageObject (с предполагаемыми локаторами)
from .auth_page import AuthPage
from .catalog_page import CatalogPage
from .cart_page import CartPage

__all__ = [
    "BasePage",
    "GuestPage",
    "LoginPage",
    "MainPage",
    "AuthPage",
    "CatalogPage",
    "CartPage",
]
