from selenium.webdriver.common.by import By


class ContactPageLocators(object):
    """Contains all of the locators used to identify objects on Contact page"""
    DROPDOWN_LIST = (By.ID, "id_contact")
    CONTACT_HEADER = (By.XPATH, "//*[text()='Contact']")
    EMAIL_FIELD = (By.ID, "email")
    ORDER_REFERENCE_FIELD = (By.ID, "id_order")
    MESSAGE_FIELD = (By.ID, 'message')
    SEND_BUTTON = (By.ID, 'submitMessage')
