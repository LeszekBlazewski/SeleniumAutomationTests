from selenium.webdriver.common.by import By


class ContactPageLocators():
    """Contains all of the locators used to identify objects on Contact page"""
    DROPDOWN_LIST = (By.ID, "id_contact")
    CONTACT_HEADER = (By.XPATH, "//*[text()='Contact']")
    EMAIL_FIELD = (By.ID, "email")
    ORDER_REFERENCE_FIELD = (By.ID, "id_order")
    MESSAGE_FIELD = (By.ID, 'message')
    ATTACHMENT_FIELD = (By.ID, 'fileUpload')
    SEND_BUTTON = (By.ID, 'submitMessage')
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert.alert-success')
    FAILURE_ALERT = (By.CSS_SELECTOR, '.alert.alert-danger')


class LoginPageLocators():
    """Conatins all of the locators used to identify objects on Login page"""
    LOGIN_HEADER = (By.XPATH, "//*[text()='Authentication']")
    EMAIL_FIELD_REGISTRATION = (By.ID, "email_create")
    EMAIL_FIELD_LOGIN = (By.ID, "email")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    SIGN_IN_BUTTON = (By.ID, "SubmitLogin")
    PASSWORD_FIELD = (By.ID, "passwd")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, ".lost_password.form-group")
    FAILURE_ALERT_WRONG_EMAIL_CREATE_ACCOUNT = (
        By.XPATH, "//*[contains(text(), 'Invalid email address')]")
    FAILURE_ALERT_WRONG_EMAIL_LOGIN = (
        By.XPATH, "//*[contains(text(), 'Invalid email')]")
    FAILURE_ALERT_WRONG_PASSWORD = (
        By.XPATH, "//*[contains(text(), 'Authentication failed')]")
    FAILURE_ALERT_BLANK_EMAIL_LOGIN = (
        By.XPATH, "//*[contains(text(), 'email address required')]")
    FAILURE_ALERT_BLANK_PASSWORD_LOGIN = (
        By.XPATH, "//*[contains(text(), 'Password is required')]")
    FAILURE_ALERT_TAKEN_EMAIL = (
        By.XPATH, "//*[contains(text(), 'already been registered')]")
    FOROGT_PASSWORD_BANNER = (
        By.XPATH, "//*[contains(text(), 'Forgot your password')]")


class RegistrationPageLocators():
    """Contains all of the locators used to indentify objects on Registration page"""
    REGISTRATION_HEADER = (
        By.XPATH, "//*[contains(text(), 'Create an account')]")
    GENDER_SELECT_BUTTON_MR = (By.ID, 'id_gender1')
    GENDER_SELECT_BUTTON_MRS = (By.ID, 'id_gender2')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#customer_firstname')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#customer_lastname')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, "passwd")
    DAYS_FIELD = (By.ID, 'days')
    MONTHS_FIELD = (By.ID, 'months')
    YEARS_FIELD = (By.ID, 'years')
    NEWSLETTER_TICK = (By.ID, 'newsletter')
    SPECIAL_OFFERS_TICK = (By.ID, 'optin')
    COMPANY_FIELD = (By.ID, 'company')
    ADDRESS_STREET_FIELD = (By.ID, 'address1')
    ADDRESS_APARTMENT_FIELD = (By.ID, 'address2')
    CITY_FIELD = (By.ID, 'city')
    STATE_FIELD = (By.ID, 'id_state')
    POSTAL_CODE_FIELD = (By.ID, 'postcode')
    COUNTRY_FIELD = (By.ID, 'id_country')
    ADDITIONAL_INFORMATION_FIELD = (By.ID, 'other')
    HOME_PHONE_FIELD = (By.ID, 'phone')
    MOBILE_PHONE_FIELD = (By.ID, 'phone_mobile')
    ALIAS_FIELD = (By.ID, 'alias')
    REGISTER_BUTTON = (By.ID, 'submitAccount')
    FAILURE_ALERT_BLANK_FIRST_NAME = (
        By.XPATH, "//b[contains(text(), 'firstname')]")
    FAILURE_ALERT_BLANK_LAST_NAME = (
        By.XPATH, "//b[contains(text(), 'lastname')]")
    FAILURE_ALERT_BLANK_EMAIL = (
        By.XPATH, "//b[contains(text(), 'email')]")
    FAILURE_ALERT_BLANK_PASSWORD = (
        By.XPATH, "//b[contains(text(), 'password')]")
    FAILURE_ALERT_BLANK_ADDRESS_STREET = (
        By.XPATH, "//b[contains(text(), 'address1')]")
    FAILURE_ALERT_BLANK_CITY = (
        By.XPATH, "//b[contains(text(), 'city')]")
    FAILURE_ALERT_NO_COUNTRY_CHOOSEN = (
        By.XPATH, "//*[contains(text(), 'Country is invalid')]")
    FAILURE_ALERT_BLANK_MOBILE_PHONE = (
        By.XPATH, "//*[contains(text(), 'You must register at least one phone number.')]")
    FAILURE_ALERT_BLANK_ALIAS = (
        By.XPATH, "//b[contains(text(), 'alias')]")
    FAILURE_ALERT_BLANK_POSTAL_CODE = (
        By.XPATH, "//*[contains(text(), 'Zip/Postal code')]")
