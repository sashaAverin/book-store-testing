import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CatalogPage(BasePage):

    PAGE_URL = Links.CATALOG_PAGE

    # locators
    HTML_FILTER_LINK = ("xpath", "//a[text()='HTML']")
    HTML_FIVE_BOOK = ("xpath", "//h3[text()='HTML5 Forms']")
    ANDROID_GUIDE_BOOK = ("xpath", "//h3[text()='Android Quick Start Guide']")
    BOOK_ITEM = ("xpath", "//li[contains(@class, 'product')]")
    SORT_BY_SELECTOR = ("xpath", "//select[@name='orderby']")
    HTML_DEV_BOOK_BUTTON = ("xpath", "//a[@data-product_id='182']")
    JS_DATA_BOOK_BUTTON = ("xpath", "//a[@data-product_id='180']")

    @allure.step("Select HTML in filters")
    def select_filter_html(self):
        self.wait.until(EC.element_to_be_clickable(self.HTML_FILTER_LINK)).click()

    @allure.step("Count quantity of products on the page")
    def number_of_product_on_page(self, number, message):
        number_of_products = self.wait.until(EC.visibility_of_all_elements_located(self.BOOK_ITEM))
        assert len(number_of_products) == number, message

    @allure.step("Open product page")
    def open_html_five_product_page(self):
        self.wait.until(EC.element_to_be_clickable(self.HTML_FIVE_BOOK)).click()

    @allure.step("Select option of sort selector")
    def select_by_value(self, value):
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(self.SORT_BY_SELECTOR)))
        dropdown.select_by_value(value)

    @allure.step("Check default option of selector")
    def check_option_of_selector(self, value, message):
        sort_by_selector = self.wait.until(EC.visibility_of_element_located(self.SORT_BY_SELECTOR))
        assert sort_by_selector.get_attribute("value") == value, message

    @allure.step("Open product page")
    def open_android_guide_product_page(self):
        self.wait.until(EC.element_to_be_clickable(self.ANDROID_GUIDE_BOOK)).click()

    @allure.step("Add book to cart")
    def add_html_dev_book_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.HTML_DEV_BOOK_BUTTON)).click()

    @allure.step("Add book to cart")
    def add_js_data_book_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.JS_DATA_BOOK_BUTTON)).click()