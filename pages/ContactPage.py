from .BasePage import BasePage, IncorrectPageException
from ..TestData import Test_Data
from SeleniumAutomationTests.Locators import ContactPageLocators
from selenium.common.exceptions import NoSuchElementException


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

    def select_subject_heading(self, messageHeading):
        self.choose_option_from_dropdown(
            *ContactPageLocators.DROPDOWN_LIST, messageHeading)

    def fill_email_address(self, email):
        self.fill_out_field(*ContactPageLocators.EMAIL_FIELD, email)

    def fill_order_reference(self, orderReference):
        self.fill_out_field(
            *ContactPageLocators.ORDER_REFERENCE_FIELD, orderReference)

    def fill_message_text(self, message):
        self.fill_out_field(*ContactPageLocators.MESSAGE_FIELD, message)

    def click_send_button(self):
        self.click(5, *ContactPageLocators.SEND_BUTTON)

    def verify_success_messag_popup(self):
        pop_up_element = None
        try:
            pop_up_element = self.find_element(
                *ContactPageLocators.SUCCESS_ALERT)
        except NoSuchElementException as e:
            print('Success pop up not found !')
            return False

        return pop_up_element.is_displayed()

    def verify_failure_message_popup(self):
        pop_up_element = None
        try:
            pop_up_element = self.find_element(
                *ContactPageLocators.FAILURE_ALERT)
        except NoSuchElementException as e:
            print('Failure pop up not found !')
            return False

        return pop_up_element.is_displayed()

    def sendMessage(self, messageHeading, email, orderReference, message):
        self.select_subject_heading(messageHeading)
        self.fill_email_address(email)
        self.fill_order_reference(orderReference)
        self.fill_message_text(message)
        self.click_send_button()
