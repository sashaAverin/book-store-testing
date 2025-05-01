from base.base_test import BaseTest

class TestLoginPage(BaseTest):

    def test_registration_on_website(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_registration_email(self.data.LOGIN)
        self.login_page.enter_registration_password(self.data.PASSWORD)
        self.login_page.click_on_registration_button()

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_on_login_button()