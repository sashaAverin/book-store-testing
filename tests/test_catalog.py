import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Catalog features")
class TestCatalog(BaseTest):

    @allure.title("Count filtered items on the page")
    @allure.severity("Major")
    @pytest.mark.functional
    def test_filter_html_books(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_my_account_link()
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_on_login_button()
        self.login_page.waiting_for_welcome_message()
        self.main_page.click_on_shop_link()
        self.catalog_page.is_opened()
        self.catalog_page.select_filter_html()
        self.catalog_page.number_of_product_on_page(3, "Количество элементов на странице не равно трём")
        self.catalog_page.make_screenshot("Filter")

    @allure.title("Sorting of products")
    @allure.severity("Major")
    @pytest.mark.functional
    def test_sort_book_by_price_desc(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_my_account_link()
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_on_login_button()
        self.login_page.waiting_for_welcome_message()
        self.main_page.click_on_shop_link()
        self.catalog_page.is_opened()
        self.catalog_page.check_option_of_selector("menu_order", "Сортировка товаров не по-умолчанию")
        self.catalog_page.select_by_value("price-desc")
        self.catalog_page.check_option_of_selector("price-desc", "Товары не отсортированы")
        self.catalog_page.make_screenshot("Sorting")