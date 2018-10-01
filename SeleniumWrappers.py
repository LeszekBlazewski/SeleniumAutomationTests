from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod
from LocatorModes import LocatorMode


class Common(object):
    """Contains wrappers for selenium methods."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, waitTime, locatorMode, Locator):
        if locatorMode == LocatorMode.ID:
            4
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, Locator)))
        elif locatorMode == LocatorMode.CLASS_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_until_element_clickable(self, waitTime, locatorMode, Locator):
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, Locator)))
        elif locatorMode == LocatorMode.CLASS_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def switch_to_window(self, windowHandle):
        self.driver.switch_to.window(windowHandle)

    def find_element(self, locatorMode, Locator):
        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(Locator)
        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(Locator)
        elif locatorMode == locatorMode.XPATH:
            element = self.driver.find_element_by_xpath(Locator)
        elif locatorMode == locatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(Locator)
        elif locatorMode == locatorMode.CLASS_NAME:
            element = self.driver.find_element_by_class_name(Locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locatorMode, Locator, text):
        self.find_element(locatorMode, Locator).clear()
        self.find_element(locatorMode, Locator).send_keys(text)

    def click(self, waitTime, locatorMode, Locator):
        self.wait_until_element_clickable(
            waitTime, locatorMode, Locator).click()
