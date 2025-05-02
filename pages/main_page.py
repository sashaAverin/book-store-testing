from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    PAGE_URL = Links.HOST

    # locators
    SELENIUM_RUBY_BOOK = ("xpath", "//h3[text()='Selenium Ruby']")

    def open_selenium_ruby_book_page(self):
        self.wait.until(EC.element_to_be_clickable(self.SELENIUM_RUBY_BOOK)).click()