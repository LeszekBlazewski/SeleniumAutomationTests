from .BasePage import BasePage, IncorrectPageException
from ..URLS import URLS
from ..Locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    """Class represents the registration panel which opens after inserting valid email address."""

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver, URLS.REGISTRATION_PAGE_URL)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(
                10, *RegistrationPageLocators.REGISTRATION_HEADER)
        except BaseException:
            raise IncorrectPageException
