from ..pages.RegistrationPage import RegistrationPage
from ..pages.LoginPage import LoginPage
from SeleniumAutomationTests.TestData import TestData
from ..Cookies import cookies
import pytest


class TestRegistrationPage():
    """Contains tests regarding registration page which opens after inserting valid email on login page."""

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_required_fields_valid_data"])
    def test_registration_required_fields_valid_data(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(  # This is necessary because registraion page can only by accessed from login page
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY, data_generator.STATE, data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        registration_page_object.click_register_button()
        assert registration_page_object.verify_title('My account')
        driver_init.add_cookie(cookies[1])
