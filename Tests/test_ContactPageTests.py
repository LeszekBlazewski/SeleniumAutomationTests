from ..pages.ContactPage import ContactPage
from SeleniumAutomationTests.TestData import Test_Data
from ..Cookies import cookies
import pytest


class TestContactPage():

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_valid_data"])
    def test_send_message_valid_data(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            Test_Data['Valid_order_reference'], 'test message',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_success_messag_popup()
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_blank_email"])
    def test_send_message_blank_email(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], '',
            Test_Data['Valid_order_reference'], 'test message',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()
        driver_init.add_cookie(cookies[1])

    @pytest.mark.xfail
    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_blank_order_reference"])
    def test_send_message_blank_order_reference(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            '', 'test message', Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_blank_message_text"])
    def test_send_message_blank_message_text(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            Test_Data['Valid_order_reference'], '',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_invalid_email"])
    def test_send_message_invalid_email(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Invalid_Email'],
            Test_Data['Valid_order_reference'], 'test message',
            Test_Data['Valid_attachment_path'])
        assert contact_page_obj.verify_failure_message_popup()
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_no_attachment"])
    def test_send_message_no_attachment(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            Test_Data['Valid_order_reference'], 'test message', '')
        assert contact_page_obj.verify_success_messag_popup()
        driver_init.add_cookie(cookies[1])
