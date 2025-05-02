from base.base_test import BaseTest

class TestProductPage(BaseTest):

    def test_product_review(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.open_selenium_ruby_book_page()
        self.product_page.click_on_review_tab()
        self.product_page.change_rating()
        self.product_page.write_review("Nice book!")
        self.product_page.fill_in_name_field("Test")
        self.product_page.fill_in_email_field("test@gmail.com")
        self.product_page.click_on_submit_button()

    def test_check_title_of_product(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_my_account_link()
        self.login_page.is_opened()
        self.login_page.enter_username(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_on_login_button()
        self.login_page.waiting_for_welcome_message()
        self.main_page.click_on_shop_link()
        self.catalog_page.open_html_five_product_page()
        self.product_page.check_title_text("HTML5 Forms")

    def test_check_sale_of_product(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_my_account_link()
        self.login_page.is_opened()
        self.login_page.enter_username(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_on_login_button()
        self.login_page.waiting_for_welcome_message()
        self.main_page.click_on_shop_link()
        self.catalog_page.open_android_guide_product_page()
        self.product_page.check_old_price("₹600.00", "Старая цена не соответствует ожидаемой")
        self.product_page.check_new_price("₹450.00", "Старая цена не соответствует ожидаемой")
        self.product_page.click_on_cover_of_book()
        self.product_page.click_on_popup_close_button()