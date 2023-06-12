from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from src.page_objects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(SearchPage, self).__init__(driver, wait_driver)

    # Find product Macbook
    def find_product_macbook(self):
        self.element("find_element_macbook").wait_clickable().click()

    # Validate price product Macbook
    def validate_price_macbook(self):
        return self.element("price_element_macbook").wait_visible().text

    # Find product iPhone
    def find_product_iphone(self):
        self.element("find_element_iphone").wait_clickable().click()

    # Validate price product iPhone
    def validate_price_iphone(self):
        return self.element("price_element_iphone").wait_visible().text

    # Find product Cinema
    def find_product_cinema(self):
        self.element("find_element_cinema").wait_clickable().click()

    # Validate price product Cinema
    def validate_price_cinema(self):
        return self.element("price_element_cinema").wait_visible().text

    # Find product Canon
    def find_product_canon(self):
        self.element("find_element_canon").wait_clickable().click()

    # Validate price product Canon
    def validate_price_canon(self):
        return self.element("price_element_canon").wait_visible().text

