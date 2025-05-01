from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    # locators
    MY_ACCOUNT_LINK = ("xpath", "//a[text()='My Account']")
    SHOP_LINK = ("xpath", "//a[text()='Shop']")
    CART_BUTTON = ("xpath", "//li[@id='wpmenucartli']")
    CART_QUANTITY_ITEMS = ("xpath", "//span[@class='cartcontents']")
    CART_PRICE_AMOUNT = ("xpath", "//span[@class='amount']")
    OVERLAY = ("xpath", "(//div[contains(@class, 'blockOverlay')])[1]")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def click_on_my_account_link(self):
        self.driver.find_element(*self.MY_ACCOUNT_LINK).click()

    def click_on_shop_link(self):
        self.driver.find_element(*self.SHOP_LINK).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def check_quantity_item_in_header(self, item_text):
        self.wait.until(EC.text_to_be_present_in_element(self.CART_QUANTITY_ITEMS, item_text))

    def check_price_item_in_header(self, price):
        self.wait.until(EC.text_to_be_present_in_element(self.CART_PRICE_AMOUNT, price))

    def waiting_for_overlay_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.OVERLAY))