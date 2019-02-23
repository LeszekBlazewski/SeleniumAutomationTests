from ..pages.ContactPage import ContactPage
from SeleniumAutomationTests.TestData import TestData
from ..Cookies import cookies
import pytest


class TestContactPage():
    """ Contains tests regarding Contact page """
    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_valid_data"])
    def test_send_message_valid_data(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            TestData.VALID_MESSAGE_HEADER, TestData.VALID_EMAIL,
            TestData.VALID_ORDER_REFERENCE, 'test message',
            TestData.VALID_ATTACHMENT_PATH)
        assert contact_page_obj.verify_popup("success")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_blank_email"])
    def test_send_message_blank_email(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            TestData.VALID_MESSAGE_HEADER, '',
            TestData.VALID_ORDER_REFERENCE, 'test message',
            TestData.VALID_ATTACHMENT_PATH)
        assert contact_page_obj.verify_popup("failure")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.xfail
    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_blank_order_reference"])
    def test_send_message_blank_order_reference(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            TestData.VALID_MESSAGE_HEADER, TestData.VALID_EMAIL,
            '', 'test message', TestData.VALID_ATTACHMENT_PATH)
        assert contact_page_obj.verify_popup("failure")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_blank_message_text"])
    def test_send_message_blank_message_text(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            TestData.VALID_MESSAGE_HEADER, TestData.VALID_EMAIL,
            TestData.VALID_ORDER_REFERENCE, '',
            TestData.VALID_ATTACHMENT_PATH)
        assert contact_page_obj.verify_popup("failure")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_invalid_email"])
    def test_send_message_invalid_email(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            TestData.VALID_MESSAGE_HEADER, TestData.INVALID_EMAIL,
            TestData.VALID_ORDER_REFERENCE, 'test message',
            TestData.VALID_ATTACHMENT_PATH)
        assert contact_page_obj.verify_popup("failure")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_send_message_no_attachment"])
    def test_send_message_no_attachment(self, driver_init):
        contact_page_obj = ContactPage(driver_init)
        contact_page_obj.sendMessage(
            TestData.VALID_MESSAGE_HEADER, TestData.VALID_EMAIL,
            TestData.VALID_ORDER_REFERENCE, 'test message', '')
        assert contact_page_obj.verify_popup("success")
        driver_init.add_cookie(cookies[1])
