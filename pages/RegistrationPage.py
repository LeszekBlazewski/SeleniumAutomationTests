from .BasePage import BasePage, IncorrectPageException
from ..URLS import URLS
from ..Locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    """Class represents the registration panel which opens after inserting valid email address."""

    def __init__(self, driver):
        super(RegistrationPage, self).__init__(
            driver, URLS.REGISTRATION_PAGE_URL)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(
                10, *RegistrationPageLocators.REGISTRATION_HEADER)
        except BaseException:
            raise IncorrectPageException

    def click_sex_button(self, sex):
        if sex == "Mr.":
            self.click(5, *RegistrationPageLocators.GENDER_SELECT_BUTTON_MR)
        else:
            self.click(5, *RegistrationPageLocators.GENDER_SELECT_BUTTON_MRS)

    def fill_first_name(self, firstName):
        self.wait_for_element_visibility(
            5, *RegistrationPageLocators.FIRST_NAME_FIELD)
        self.fill_out_field(
            *RegistrationPageLocators.FIRST_NAME_FIELD, firstName)

    def fill_last_name(self, lastName):
        self.fill_out_field(
            *RegistrationPageLocators.LAST_NAME_FIELD, lastName)

    def fill_password(self, password):
        self.fill_out_field(*RegistrationPageLocators.PASSWORD_FIELD, password)

    def select_date_of_birth(self, day, month, year):
        self.choose_option_from_dropdown(
            *RegistrationPageLocators.DAYS_FIELD, day)
        self.choose_option_from_dropdown(
            *RegistrationPageLocators.MONTHS_FIELD, month)
        self.choose_option_from_dropdown(
            *RegistrationPageLocators.YEARS_FIELD, year)

    def mark_tick_boxes(self, newsletter, specialOffers):
        if newsletter == "yes":
            self.click(5, *RegistrationPageLocators.NEWSLETTER_TICK)
        if specialOffers == "yes":
            self.click(5, *RegistrationPageLocators.SPECIAL_OFFERS_TICK)

    def fill_company_field(self, companyName):
        self.fill_out_field(*RegistrationPageLocators.COMPANY_FIELD)

    def fill_address(self, street, buildingNumber):
        self.fill_out_field(
            *RegistrationPageLocators.ADDRESS_STREET_FIELD, street)
        self.fill_out_field(
            *RegistrationPageLocators.ADDRESS_APARTMENT_FIELD, buildingNumber)

    def fill_city_field(self, cityName):
        self.fill_out_field(*RegistrationPageLocators.CITY_FIELD, cityName)

    def choose_country(self, country, state, postalCode):
        self.choose_option_from_dropdown(
            *RegistrationPageLocators.COUNTRY_FIELD, country)
        if country == "United States":
            self.choose_option_from_dropdown(
                *RegistrationPageLocators.STATE_FIELD, state)
            self.fill_out_field(
                *RegistrationPageLocators.POSTAL_CODE_FIELD, postalCode)

    def fill_additional_information(self, information):
        self.fill_out_field(
            *RegistrationPageLocators.ADDITIONAL_INFORMATION_FIELD, information)

    def fill_phone_fields(self, homePhone, mobilePhone):
        self.fill_out_field(
            *RegistrationPageLocators.HOME_PHONE_FIELD, homePhone)
        self.fill_out_field(
            *RegistrationPageLocators.MOBILE_PHONE_FIELD, mobilePhone)

    def fill_alias_field(self, alias):
        self.fill_out_field(*RegistrationPageLocators.ALIAS_FIELD, alias)

    def click_register_button(self):
        self.click(5, *RegistrationPageLocators.REGISTER_BUTTON)

    def fill_required_fields_for_registration(self, firstName, lastName, password, addressStreet, addressBuilding, country, state, postalCode, city, mobilePhone, alias):
        self.fill_first_name(firstName)
        self.fill_last_name(lastName)
        self.fill_password(password)
        self.fill_address(addressStreet, addressBuilding)
        self.fill_city_field(city)
        self.choose_country(country, state, postalCode)
        self.fill_phone_fields("", mobilePhone)
        self.fill_alias_field(alias)
