from .BasePage import BasePage, IncorrectPageException
from ..URLS import URLS
from ..Locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    """Class represents the logging page."""

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver, URLS.LOGIN_PAGE_URL)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(
                10, *LoginPageLocators.LOGIN_HEADER)
        except BaseException:
            raise IncorrectPageException

    def fill_email_address_registration(self, email):
        self.fill_out_field(*LoginPageLocators.EMAIL_FIELD_REGISTRATION, email)

    def fill_email_address_login(self, email):
        self.fill_out_field(*LoginPageLocators.EMAIL_FIELD_LOGIN, email)

    def fill_password(self, password):
        self.fill_out_field(*LoginPageLocators.PASSWORD_FIELD, password)

    def click_create_account_button(self):
        self.click(5, *LoginPageLocators.CREATE_ACCOUNT_BUTTON)

    def click_sign_in_button(self):
        self.click(5, *LoginPageLocators.SIGN_IN_BUTTON)

    def click_forgot_password_link(self):
        self.click(5, *LoginPageLocators.FORGOT_PASSWORD_LINK)

    def verify_popup(self, type):
        pop_up_element = None
        try:
            if type == "wrong_email_create_account":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FAILURE_ALERT_WRONG_EMAIL_CREATE_ACCOUNT)
            elif type == "wrong_email_log_in":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FAILURE_ALERT_WRONG_EMAIL_LOGIN)
            elif type == "wrong_password_log_in":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FAILURE_ALERT_WRONG_PASSWORD)
            elif type == "blank_email_log_in":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FAILURE_ALERT_BLANK_EMAIL_LOGIN)
            elif type == "blank_password_log_in":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FAILURE_ALERT_BLANK_PASSWORD_LOGIN)
            elif type == "taken_email_create_account":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FAILURE_ALERT_TAKEN_EMAIL)
            elif type == "forgot_password_banner":
                pop_up_element = self.wait_for_element_visibility(
                    5, *LoginPageLocators.FOROGT_PASSWORD_BANNER)
        except NoSuchElementException as e:
            print('Failure pop up not found !')
            return False

        return pop_up_element.is_displayed()

    def log_in(self, email, password):
        self.fill_email_address_login(email)
        self.fill_password(password)
        self.click_sign_in_button()

    def fill_create_account_panel(self, email):
        self.fill_email_address_registration(email)
        self.click_create_account_button()

    def verify_title(self, title):
        if title in self.driver.title:
            return True
        else:
            return False

    def print_me(self):
        print(self.driver.title)
