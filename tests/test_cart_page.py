from base.base_test import BaseTest

class TestCartPage(BaseTest):

    def test_subtotal_amount(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_shop_link()
        self.catalog_page.add_html_dev_book_to_cart()
        self.main_page.check_quantity_item_in_header("1 Item")
        self.main_page.check_price_item_in_header("₹180.00")
        self.main_page.go_to_cart()
        self.cart_page.check_subtotal_amount("₹180.00", "Промежуточная стоимость не равна 180")
        self.cart_page.check_total_price("₹180.00", "Окончательная стоимость не равна 180")

    def test_work_in_cart(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_shop_link()
        self.catalog_page.is_opened()
        self.catalog_page.add_html_dev_book_to_cart()
        self.main_page.check_quantity_item_in_header("1 Item")
        self.catalog_page.add_js_data_book_to_cart()
        self.main_page.check_quantity_item_in_header("2 Item")
        self.main_page.go_to_cart()
        self.cart_page.is_opened()
        self.cart_page.remove_first_item_from_cart()
        self.cart_page.cancel_item_removal()
        self.cart_page.change_quantity_of_item("3")
        self.cart_page.update_cart()
        self.cart_page.check_quantity_item_in_cart("3", "Количество товара не соответствует")
        self.cart_page.waiting_for_overlay_disappear()
        self.cart_page.click_on_apply_coupon_button()
        self.cart_page.waiting_for_overlay_disappear()
        self.cart_page.check_error_message("Please enter a coupon code.", "Сообщение об ошибке не верно")
