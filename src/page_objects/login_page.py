import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(LoginPage, self).__init__(driver, wait_driver)

    # Loggin with user data
    def login(self, email: str, password: str):
        logging.info(f"Login with email address {email} and password *****")
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("login_btn").wait_clickable().click()

    # Get warning message
    def get_warning_message(self):
        return self.element("warning_message").wait_visible().text

    # Get message to forgot password
    def get_success_msg_forgot_p(self):
        return self.element("alert_success").wait_visible().text

    # Method to validate process forgot password
    def forgot_password(self, email: str):
        logging.info(f"Forgot password {email}*****")
        self.element("forgot_link").wait_clickable().click()
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("continue_button").wait_clickable().click()
