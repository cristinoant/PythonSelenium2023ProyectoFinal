import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from src.page_objects.base_page import BasePage


class PurchasePage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(PurchasePage, self).__init__(driver, wait_driver)

    def login(self, email: str, password: str):
        logging.info(f"Login with email address {email} and password *****")
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("login_btn").wait_clickable().click()

    # Find menu Phones and PDAs
    def click_product_phones(self):
        self.element("find_phones_and_pdas_menu").wait_clickable().click()

    # Add to cart HTC item
    def add_to_cart_htc(self):
        self.element("add_to_cart_phone_htc").wait_clickable().click()

    # Add to cart iPhone item
    def add_to_cart_iphone(self):
        self.element("add_to_cart_phone_iphone").wait_clickable().click()

    # Add to cart Palm item
    def add_to_cart_palm(self):
        self.element("add_to_cart_phone_palm").wait_clickable().click()

    # Find Menu Cameras
    def find_cameras(self):
        self.element("find_cameras_menu").wait_clickable().click()

    # Add to cart Nikon item
    def add_to_cart_camera(self):
        self.element("add_to_cart_camera_nikon").wait_clickable().click()

    # Press button Checkout
    def validate_checkout_items(self):
        self.element("validate_checkout").wait_clickable().click()

    # Validate HTC Item in cart
    def validate_htc_in_cart(self):
        self.element("htc_in_cart").wait_visible()

    # Validate Palm Item in cart
    def validate_palm_in_cart(self):
        self.element("palm_in_cart").wait_clickable()

    # Validate iPhone Item in cart
    def validate_iphone_in_cart(self):
        self.element("iphone_in_cart").wait_visible()

    # Validate Nikon Item in cart
    def validate_camera_in_cart(self):
        self.element("camera_in_cart").wait_clickable()

    # Validate Subtotal Amount
    def validate_subtotal(self):
        return self.element("validate_subtotal_amount").wait_visible().text

    # Validate Total Amount
    def validate_total(self):
        return self.element("validate_total_amount").wait_clickable().text
