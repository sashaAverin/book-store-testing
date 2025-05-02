import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirm_order_page import ConfirmOrderPage

class BaseTest:

    data: Data

    login_page: LoginPage
    product_page: ProductPage
    main_page: MainPage
    catalog_page: CatalogPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    confirm_order_page: ConfirmOrderPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.product_page = ProductPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.catalog_page = CatalogPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)
        request.cls.confirm_order_page = ConfirmOrderPage(driver)