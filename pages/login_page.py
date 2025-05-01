from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    # locators
    EMAIL_REG_FIELD = ("xpath", "//input[@id='reg_email']")
    PASSWORD_REG_FIELD = ("xpath", "//input[@id='reg_password']")
    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//input[@name='login']")
    REG_BUTTON = ("xpath", "//input[@name='register']")
    WELCOME_MESSAGE = ("xpath", "//div[@class='woocommerce-MyAccount-content']")

    def enter_registration_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_REG_FIELD)).send_keys(email)

    def enter_registration_password(self, password):
        reg_password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_REG_FIELD))
        reg_password.send_keys(password)
        reg_password.send_keys("A")

    def click_on_registration_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REG_BUTTON)).click()

    def enter_username(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_on_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def waiting_for_welcome_message(self):
        self.wait.until(EC.visibility_of_element_located(self.WELCOME_MESSAGE))