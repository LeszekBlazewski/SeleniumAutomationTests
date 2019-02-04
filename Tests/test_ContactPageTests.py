from .BaseTestCase import BaseTestClass
from ..pages.ContactPage import ContactPage
from SeleniumAutomationTests.TestData import Test_Data
from ..LocatorModes import LocatorMode
from ..DriverSettings import Driver_Settings
import pytest


class ContactPageTests(BaseTestClass):

    def setUp(self):
        super(ContactPageTests, self).setUp()
        self.navigate_to_page(Driver_Settings['Contact_page_URL'])

    def test_send_message_valid_data(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            Test_Data['Valid_order_reference'], 'test message',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_success_messag_popup()

    def test_send_message_blank_email(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], '',
            Test_Data['Valid_order_reference'], 'test message',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()

    @pytest.mark.xfail
    def test_send_message_blank_order_reference(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            '', 'test message', Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()

    def test_send_message_blank_message_text(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            Test_Data['Valid_order_reference'], '',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()

    def test_send_message_invalid_email(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Invalid_Email'],
            Test_Data['Valid_order_reference'], 'test message',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()

    def test_send_message_no_attachment(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            Test_Data['Valid_order_reference'], 'test message', '')
        assert contact_page_obj.verify_success_messag_popup()
