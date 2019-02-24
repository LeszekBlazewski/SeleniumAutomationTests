from .BasePage import BasePage, IncorrectPageException
from ..URLS import URLS
from SeleniumAutomationTests.Locators import ContactPageLocators
from selenium.common.exceptions import TimeoutException, InvalidArgumentException


class ContactPage(BasePage):
    """Class represents the contact page."""

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver, URLS.CONTACT_PAGE_URL)

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

    def fill_atachment_field(self, filename):
        try:
            self.fill_out_field(
                *ContactPageLocators.ATTACHMENT_FIELD, filename)
        except InvalidArgumentException as e:
            print('File name specified in test does not exist !')

    def verify_popup(self, type):
        pop_up_element = None
        try:
            if type == "success":
                pop_up_element = self.wait_for_element_visibility(
                    5, *ContactPageLocators.SUCCESS_ALERT)
            else:
                pop_up_element = self.wait_for_element_visibility(
                    5, *ContactPageLocators.FAILURE_ALERT)
        except TimeoutException as e:
            if type == 'success':
                print('Success pop up not found !')
            else:
                print('Failure pop up not found !')
            return False

        return pop_up_element.is_displayed()

    def sendMessage(self, messageHeading, email, orderReference, message, attachmentName):
        self.select_subject_heading(messageHeading)
        self.fill_email_address(email)
        self.fill_order_reference(orderReference)
        self.fill_atachment_field(attachmentName)
        self.fill_message_text(message)
        self.click_send_button()
