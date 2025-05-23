import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

    PAGE_URL = Links.CART_PAGE

    # locators
    REMOVE_FIRST_ITEM_BUTTON = ("xpath", "(//a[@class='remove'])[1]")
    UNDO_BUTTON = ("xpath", "//a[text()='Undo?']")
    QUANTITY_INPUT = ("xpath", "(//input[@type='number'])[2]")
    UPDATE_CART_BUTTON = ("xpath", "//input[@name='update_cart']")
    APPLY_COUPON_BUTTON = ("xpath", "//input[@name='apply_coupon']")
    ERROR_MESSAGE = ("xpath", "//ul[@class='woocommerce-error']")
    SUBTOTAL_AMOUNT = ("xpath", "//td[@data-title='Subtotal']")
    TOTAL_AMOUNT = ("xpath", "//td[@data-title='Total']")
    CHECKOUT_BUTTON = ("xpath", "//div[@class='wc-proceed-to-checkout']//a")

    @allure.step("Check subtotal price")
    def check_subtotal_price(self, price, message):
        subtotal_amount = self.wait.until(EC.visibility_of_element_located(self.SUBTOTAL_AMOUNT))
        assert subtotal_amount.text == price, message

    @allure.step("Check total price")
    def check_total_price(self, price, message):
        total_price = self.wait.until(EC.visibility_of_element_located(self.TOTAL_AMOUNT))
        assert total_price.text == price, message

    @allure.step("Remove item from the cart")
    def remove_first_item_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_FIRST_ITEM_BUTTON)).click()

    @allure.step("Cancel item removal")
    def cancel_item_removal(self):
        self.wait.until(EC.visibility_of_element_located(self.UNDO_BUTTON)).click()

    @allure.step("Change quantity of item")
    def change_quantity_of_item(self, number):
        quantity_item = self.wait.until(EC.element_to_be_clickable(self.QUANTITY_INPUT))
        quantity_item.clear()
        quantity_item.send_keys(number)

    @allure.step("Update our cart")
    def update_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.UPDATE_CART_BUTTON)).click()

    @allure.step("Check quantity of item")
    def check_quantity_item_in_cart(self, number, message):
        quantity_item = self.wait.until(EC.element_to_be_clickable(self.QUANTITY_INPUT)).get_attribute("value")
        assert quantity_item == number, message

    @allure.step("Click on apply coupon button")
    def click_on_apply_coupon_button(self):
        self.wait.until(EC.element_to_be_clickable(self.APPLY_COUPON_BUTTON)).click()

    @allure.step("Check error message")
    def check_error_message(self, text, message):
        error_message = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        assert error_message.text == text, message

    @allure.step("Click on checkout button")
    def click_on_checkout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()