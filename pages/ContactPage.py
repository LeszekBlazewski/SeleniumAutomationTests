from .BasePage import BasePage, IncorrectPageException
from ..TestData import Test_Data
from SeleniumAutomationTests.Locators import ContactPageLocators


class ContactPage(BasePage):
    """Class represents the contact page."""

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(
                10, *ContactPageLocators.CONTACT_HEADER)
        except BaseException:
            raise IncorrectPageException

    def sendMessage(self, messageHeading, email, orderReference, message):
        self.choose_option_from_dropdown(
            *ContactPageLocators.DROPDOWN_LIST, messageHeading)
        self.fill_out_field(*ContactPageLocators.EMAIL_FIELD, email)
        self.fill_out_field(
            *ContactPageLocators.ORDER_REFERENCE_FIELD, orderReference)
        self.fill_out_field(*ContactPageLocators.MESSAGE_FIELD, message)
        self.click(5, *ContactPageLocators.SEND_BUTTON)
