from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod
from LocatorModes import LocatorMode


class BasePage(object):
    """Class represents the base page."""

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

        @abstractmethod
        def _verify_page(self):
            """This method verifies that we are on the correct page."""

    def wait_for_element_visibility(self, waitTime, locatorMode, locator):
        if locatorMode == LocatorMode.ID:
            4
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.ID, locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.NAME, locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.XPATH, locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, locator)))
        elif locatorMode == LocatorMode.CLASS_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_until_element_clickable(self, waitTime, locatorMode, locator):
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.ID, locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.NAME, locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.XPATH, locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator)))
        elif locatorMode == LocatorMode.CLASS_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def switch_to_window(self, windowHandle):
        self.driver.switch_to.window(windowHandle)

    def find_element(self, locatorMode, locator):
        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(locator)
        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(locator)
        elif locatorMode == locatorMode.XPATH:
            element = self.driver.find_element_by_xpath(locator)
        elif locatorMode == locatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(locator)
        elif locatorMode == locatorMode.CLASS_NAME:
            element = self.driver.find_element_by_class_name(locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locatorMode, locator, text):
        self.find_element(locatorMode, locator).clear()
        self.find_element(locatorMode, locator).send_keys(text)

    def click(self, waitTime, locatorMode, locator):
        self.wait_until_element_clickable(
            waitTime, locatorMode, locator).click()


class IncorrectPageException(Exception):
    """ This exception should be thrown when trying to instantiate the wrong page. """
