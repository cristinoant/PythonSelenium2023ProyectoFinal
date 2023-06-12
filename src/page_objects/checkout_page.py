import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from src.page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(CheckoutPage, self).__init__(driver, wait_driver)

    def login(self, email: str, password: str):
        logging.info(f"Login with email address {email} and password *****")
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("login_btn").wait_clickable().click()

    # Select checkout button
    def click_checkout(self):
        self.element("checkout_btn").wait_clickable().click()

    # Select new address button
    def new_address(self):
        self.element("new_address_btn").wait_clickable().click()

    # Fill items
    def fill_items(self, first_name: str, lastname: str, company: str, address1: str, city: str, post_code: str, country: str):
        self.element("firstname_input").wait_visible().send_keys(first_name)
        self.element("lastname_input").wait_visible().send_keys(lastname)
        self.element("company_input").wait_visible().send_keys(company)
        self.element("address1_input").wait_visible().send_keys(address1)
        self.element("city_input").wait_visible().send_keys(city)
        self.element("post_code_input").wait_visible().send_keys(post_code)
        #self.element("country_input").select_by_value() # 138 to Mexico
        # self.element("input-payment-zone").select_by_value() # 2153 to CDMX

    # TODO Modify method for select item by value HELP Teacher!!!
    def input_payment_country(self):
        select = Select(self.input_payment_country())
        select.select_by_value("country_input")

    # Press button continue Section Billing Details
    def continue_btn_payment(self):
        self.element("continue_payment_btn").wait_clickable().click()

    # Select radio button Existing address Section Delivery Details
    def radio_btn_adress(self):
        self.element("existing_address_radio_btn").wait_clickable().click()

    # Press button continue Section Delivery Details
    def continue_delivery_btn_method(self):
        self.element("continue_delivery_method_btn").wait_clickable().click()

    # Press button continue Section Delivery Method
    def contiue_btn_shipping_method(self):
        self.element("continue_shipping_method_btn").wait_clickable().click()

    # Press checkbox Terms & Conditions Section Payment Method
    def checkbox_agree(self):
        self.element("checkbox_agree_checkbox").wait_clickable().click()

    # Press button continue Section Payment Method
    def continue_btn_payment_method(self):
        self.element("continue_payment_method_btn").wait_clickable().click()

    # Validate Subtotal amount
    def validate_subtotal(self):
        return self.element("subtotal_amount").wait_visible().text

    # Validate Total amount
    def validate_total(self):
        return self.element("total_amount").wait_clickable().text

    # Press confirm order
    def confirm_order(self):
        self.element("confirm_btn_order").wait_clickable().click()
