import random
import time
import allure
from base.base_page import BasePage
from config.links import Links

from selenium.webdriver.support import expected_conditions as EC

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

    @allure.step("Enter registration email")
    def enter_registration_email(self, email):
        reg_email = self.wait.until(EC.element_to_be_clickable(self.EMAIL_REG_FIELD))
        reg_email.send_keys(f"{email}{random.randint(100, 999)}@gmail.com")

    @allure.step("Enter registration password")
    def enter_registration_password(self, password):
        password_input = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_REG_FIELD))
        time.sleep(3)
        password_input.send_keys(password)

    @allure.step("Click submit button")
    def click_on_registration_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REG_BUTTON)).click()

    @allure.step("Enter login")
    def enter_username(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_on_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    @allure.step("Registration has been successfully")
    def waiting_for_welcome_message(self):
        self.wait.until(EC.visibility_of_element_located(self.WELCOME_MESSAGE))