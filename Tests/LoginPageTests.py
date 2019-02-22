from ..pages.LoginPage import LoginPage
from SeleniumAutomationTests.TestData import TestData
from ..Cookies import cookies
import pytest


class TestLoginPage():
    """Contains tests regarding Login page """

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_login_valid_data"])
    def test_login_valid_data(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.log_in(
            TestData.VALID_EMAIL,
            TestData.VALID_PASSWORD)
        assert login_page_object.verify_title('My account')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_login_invalid_email_address"])
    def test_login_invalid_email_address(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.log_in(
            TestData.INVALID_EMAIL,
            TestData.VALID_PASSWORD)
        assert login_page_object.verify_popup("wrong_email_log_in")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_login_invalid_password"])
    def test_login_invalid_password(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.log_in(
            TestData.VALID_EMAIL,
            TestData.INVALID_PASSWORD)
        assert login_page_object.verify_popup("wrong_password_log_in")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_login_blank_email"])
    def test_login_blank_email(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.log_in(
            '',
            TestData.VALID_PASSWORD)
        assert login_page_object.verify_popup("blank_email_log_in")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_login_blank_password"])
    def test_login_blank_password(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.log_in(
            TestData.VALID_EMAIL,
            '')
        assert login_page_object.verify_popup("blank_password_log_in")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_create_account_valid_email"])
    def test_create_account_valid_email(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        assert login_page_object.verify_title("Login")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_create_account_invalid_email"])
    def test_create_account_invalid_email(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(TestData.INVALID_EMAIL)
        assert login_page_object.verify_popup("wrong_email_create_account")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_create_account_blank_email"])
    def test_create_account_blank_email(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel('')
        assert login_page_object.verify_popup("wrong_email_create_account")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_create_account_taken_email"])
    def test_create_account_taken_email(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(TestData.VALID_EMAIL)
        assert login_page_object.verify_popup("taken_email_create_account")
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_forgot_password_link"])
    def test_forgot_password_link(self, driver_init):
        login_page_object = LoginPage(driver_init)
        login_page_object.click_forgot_password_link()
        assert login_page_object.verify_popup("forgot_password_banner")
        driver_init.add_cookie(cookies[1])
