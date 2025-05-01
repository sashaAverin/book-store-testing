from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ConfirmOrderPage(BasePage):

    # locators
    CONFIRM_MESSAGE = ("xpath", "//p[@class='woocommerce-thankyou-order-received']")
    PAYMENT_METHOD_TEXT = ("xpath", "(//table[@class='shop_table order_details']//td)[5]")

    def check_confirm_message(self, text, message):
        confirm_message = self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MESSAGE))
        assert confirm_message.text == text, message

    def check_payment_method(self, text, message):
        payment_method = self.wait.until(EC.visibility_of_element_located(self.PAYMENT_METHOD_TEXT))
        assert payment_method.text == text, message