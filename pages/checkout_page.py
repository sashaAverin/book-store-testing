from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class CheckoutPage(BasePage):

    PAGE_URL = Links.CHECKOUT_PAGE

    # locators
    FIRST_NAME_FIELD = ("xpath", "//input[@id='billing_first_name']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='billing_last_name']")
    EMAIL_FIELD = ("xpath", "//input[@id='billing_email']")
    PHONE_FIELD = ("xpath", "//input[@id='billing_phone']")
    COUNTRY_FIELD = ("xpath", "//div[@id='s2id_billing_country']//a")
    COUNTRY_FIELD_INPUT = ("xpath", "//input[@id='s2id_autogen1_search']")
    ADDRESS_FIELD = ("xpath", "//input[@id='billing_address_1']")
    CITY_FIELD = ("xpath", "//input[@id='billing_city']")
    COUNTRY_POST_FIELD = ("xpath", "//div[@id='s2id_billing_state']//a")
    COUNTRY_POST_FIELD_INPUT = ("xpath", "//input[@id='s2id_autogen2_search']")
    POSTCODE_FIELD = ("xpath", "//input[@id='billing_postcode']")
    PAYMENT_METHOD_RADIO = ("xpath", "//input[@id='payment_method_cheque']")
    ORDER_BUTTON = ("xpath", "//input[@id='place_order']")

    def enter_first_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(name)

    def enter_last_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(name)

    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def enter_phone(self, phone):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD)).send_keys(phone)

    def select_country(self, country):
        country_field = self.wait.until(EC.element_to_be_clickable(self.COUNTRY_FIELD))
        country_field.click()
        country_input = self.wait.until(EC.element_to_be_clickable(self.COUNTRY_FIELD_INPUT))
        country_input.send_keys(country + Keys.ENTER)

    def enter_address(self, address):
        self.wait.until(EC.element_to_be_clickable(self.ADDRESS_FIELD)).send_keys(address)

    def enter_city(self, city):
        self.wait.until(EC.element_to_be_clickable(self.CITY_FIELD)).send_keys(city)

    def select_country_post(self, country):
        country_post_field = self.wait.until(EC.element_to_be_clickable(self.COUNTRY_POST_FIELD))
        country_post_field.click()
        country_post_input = self.wait.until(EC.element_to_be_clickable(self.COUNTRY_POST_FIELD_INPUT))
        country_post_input.send_keys(country + Keys.ENTER)

    def enter_post_code(self, postcode):
        self.wait.until(EC.element_to_be_clickable(self.POSTCODE_FIELD)).send_keys(postcode)

    def click_on_payment_method_radio(self):
        payment_method = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_METHOD_RADIO))
        payment_method.click()
        payment_method.is_selected()

    def click_on_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()