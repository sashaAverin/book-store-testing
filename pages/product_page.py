from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    # locators
    REVIEWS_TAB = ("xpath", "//li[@class='reviews_tab']")
    FIVE_STAR = ("xpath", "//a[@class='star-5']")
    REVIEW_TEXTAREA = ("xpath", "//textarea[@id='comment']")
    NAME_FIELD = ("xpath", "//input[@id='author']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    SUBMIT_BUTTON = ("xpath", "//input[@id='submit']")
    TITLE_TEXT = ("xpath", "//h1")
    OLD_PRICE = ("xpath", "//del")
    NEW_PRICE = ("xpath", "//p[@class='price']//ins")
    COVER_BOOK = ("xpath", "//div[@class='images']")
    POPUP_CLOSE_BUTTON = ("xpath", "//a[@class='pp_close']")

    def click_on_review_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.REVIEWS_TAB)).click()

    def change_rating(self):
        self.wait.until(EC.element_to_be_clickable(self.FIVE_STAR)).click()

    def write_review(self, review):
        self.wait.until(EC.element_to_be_clickable(self.REVIEW_TEXTAREA)).send_keys(review)

    def fill_in_name_field(self, name):
        self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)

    def fill_in_email_field(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def click_on_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def check_title_text(self, expected_text):
        title_text = self.wait.until(EC.visibility_of_element_located(self.TITLE_TEXT))
        assert title_text.text == expected_text, "Заголовок книги не совпадает"

    def check_old_price(self, price, message):
        old_price = self.wait.until(EC.visibility_of_element_located(self.OLD_PRICE))
        assert old_price.text == price, message

    def check_new_price(self, price, message):
        new_price = self.wait.until(EC.visibility_of_element_located(self.NEW_PRICE))
        assert new_price.text == price, message

    def click_on_cover_of_book(self):
        self.wait.until(EC.element_to_be_clickable(self.COVER_BOOK)).click()

    def click_on_popup_close_button(self):
        self.wait.until(EC.element_to_be_clickable(self.POPUP_CLOSE_BUTTON)).click()
# old_price = wait.until(EC.visibility_of_element_located(OLD_PRICE))
# assert old_price.text == "₹600.00", "Старая цена не соответствует ожидаемой"
#
# new_price = wait.until(EC.visibility_of_element_located(NEW_PRICE))
# assert new_price.text == "₹450.00", "Старая цена не соответствует ожидаемой"
#
# wait.until(EC.element_to_be_clickable(COVER_BOOK)).click()
# wait.until(EC.element_to_be_clickable(POPUP_CLOSE_BUTTON)).click()