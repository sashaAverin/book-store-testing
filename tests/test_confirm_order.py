import allure
import pytest
import random
from base.base_test import BaseTest

@allure.feature("Order")
class TestConfirmOrderPage(BaseTest):

    @allure.title("Confirmation of order")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_order(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_shop_link()
        self.catalog_page.is_opened()
        self.catalog_page.add_html_dev_book_to_cart()
        self.main_page.check_quantity_item_in_header("1 Item")
        self.main_page.go_to_cart()
        self.cart_page.is_opened()
        self.cart_page.click_on_checkout_button()
        self.checkout_page.is_opened()
        self.checkout_page.enter_first_name("testFirstName")
        self.checkout_page.enter_last_name("testLastName")
        self.checkout_page.enter_email("testEmail@gmail.com")
        self.checkout_page.enter_phone("+1(345)273-45-12")
        self.checkout_page.select_country("Hungary")
        self.checkout_page.enter_address("Andrassy Avenue")
        self.checkout_page.enter_city("Budapest")
        self.checkout_page.select_country_post("Budapest")
        self.checkout_page.enter_post_code(f"{random.randint(100000, 999999)}")
        self.cart_page.waiting_for_overlay_disappear()
        self.checkout_page.click_on_payment_method_radio()
        self.cart_page.waiting_for_overlay_disappear()
        self.checkout_page.click_on_order_button()
        self.confirm_order_page.check_confirm_message("Thank you. Your order has been received.", "Текст сообщения с подтверждением не верный")
        self.confirm_order_page.check_payment_method("Check Payments", "Отображается не верный способ доставки товара")
        self.confirm_order_page.make_screenshot("Success")