import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Authorization")
class TestLoginPage(BaseTest):

    @allure.title("Registration in system")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_registration_on_website(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_registration_email(self.data.REG_EMAIL)
        self.login_page.enter_registration_password(self.data.PASSWORD)
        self.login_page.click_on_registration_button()
        self.login_page.waiting_for_welcome_message()
        self.login_page.make_screenshot("Success")

    @allure.title("Log in to the system")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_log_in_to_account(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_on_login_button()
        self.login_page.waiting_for_welcome_message()
        self.login_page.make_screenshot("Success")