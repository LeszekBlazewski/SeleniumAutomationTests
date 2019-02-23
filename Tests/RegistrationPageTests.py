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
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_title('My account')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_first_name"])
    def test_registration_empty_first_name(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            "",
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_first_name')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_last_name"])
    def test_registration_empty_last_name(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            "",
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_last_name')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_email"])
    def test_registration_empty_email(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            "",
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_email')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.xfail
    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_password"])
    def test_registration_empty_password(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            "",
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_password')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_address"])
    def test_registration_empty_address_street(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            "",
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_address_street')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_address_building"])
    def test_registration_empty_address_building(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            "",
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        # because second address field is optional, so we should land on page with successfull account creation
        assert registration_page_object.verify_title('My account')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_city"])
    def test_registration_empty_city(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            "",
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_city')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_no_country_choosen"])
    def test_registration_no_country_choosen(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            '-',
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('no_country_choosen')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_mobile_phone"])
    def test_registration_empty_mobile_phone(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            '',
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_mobile_phone')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_only_home_phone"])
    def test_registration_only_home_phone(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_phone_fields(
            data_generator.PHONE_NUMBER, '')
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            '',
            data_generator.ALIAS)
        # because only one phone is required, so we should land on page with successfull account creation
        assert registration_page_object.verify_title('My account')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_alias"])
    def test_registration_empty_alias(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            data_generator.POSTAL_CODE,
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            '')
        assert registration_page_object.verify_popup('blank_alias')
        driver_init.add_cookie(cookies[1])

    @pytest.mark.parametrize('setUp_test_information_for_zelenium',
                             ["test_registration_empty_postal_code"])
    def test_registration_empty_postal_code(self, driver_init, data_generator):
        login_page_object = LoginPage(driver_init)
        login_page_object.fill_create_account_panel(
            data_generator.RANDOM_EMAIL)
        registration_page_object = RegistrationPage(driver_init)
        registration_page_object.fill_required_fields_for_registration(
            data_generator.FIRST_NAME,
            data_generator.LAST_NAME,
            data_generator.RANDOM_EMAIL,
            data_generator.RANDOM_PASSWORD,
            data_generator.ADDRESS_STREET,
            data_generator.ADDRESS_BUILDING,
            TestData.COUNTRY,
            data_generator.STATE,
            '',
            data_generator.CITY,
            data_generator.PHONE_NUMBER,
            data_generator.ALIAS)
        assert registration_page_object.verify_popup('blank_postal_code')
        driver_init.add_cookie(cookies[1])
