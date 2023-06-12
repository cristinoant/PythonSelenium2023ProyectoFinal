import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    # Register a user
    def register(self, first_name: str, last_name: str, email: str, telephone: str, password: str, confirm_password: str):
        logging.info(f"Register new User with {first_name, last_name, email, telephone} and password *****")
        self.element("first_name_input").wait_clickable().send_keys(first_name)
        self.element("last_name_input").wait_clickable().send_keys(last_name)
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("telephone_input").wait_clickable().send_keys(telephone)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("confirm_password").wait_clickable().send_keys(confirm_password)
        self.element("checkbox_terms").wait_clickable().click()
        # self.element("login_btn").wait_clickable().click()

    # Register a user whith email existing in DB
    def email_alredy_register(self, first_name: str, last_name: str, email: str, telephone: str, password: str, confirm_password: str):
        logging.info(f"Register new User with {first_name, last_name, email, telephone} and password *****")
        self.element("first_name_input").wait_clickable().send_keys(first_name)
        self.element("last_name_input").wait_clickable().send_keys(last_name)
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("telephone_input").wait_clickable().send_keys(telephone)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("confirm_password").wait_clickable().send_keys(confirm_password)
        self.element("checkbox_terms").wait_clickable().click()
        self.element("continue_btn").wait_clickable().click()

    # Register a user and don't press checkbox Privacy Policy
    def missing_checkbox_select(self, first_name: str, last_name: str, email: str, telephone: str, password: str, confirm_password: str):
        logging.info(f"Register new User with {first_name, last_name, email, telephone} and password *****")
        self.element("first_name_input").wait_clickable().send_keys(first_name)
        self.element("last_name_input").wait_clickable().send_keys(last_name)
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("telephone_input").wait_clickable().send_keys(telephone)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("confirm_password").wait_clickable().send_keys(confirm_password)
        self.element("continue_btn").wait_clickable().click()

    # Get warning message when email is already register in system
    def get_warning_message_email_already(self):
        return self.element("email_already_msg").wait_visible().text

    # Get warning message when don't press checkbox Privacy Policy
    def get_warning_message_checkbox_select(self):
        return self.element("email_already_msg").wait_visible().text
