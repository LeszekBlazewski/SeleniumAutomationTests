from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod
from ..Cookies import cookies


class BasePage(object):
    """Class represents the base page. Functions as a base schema for all
    pages."""

    def __init__(self, driver, page_url):
        self.driver = driver
        self.driver.get(page_url)
        self.driver.add_cookie(cookies[0])
        self._verify_page()

        @abstractmethod
        def _verify_page(self):
            """This method verifies that we are on the correct page."""

    def wait_for_element_visibility(self, waitTime, locatorMode, locator):
        if locatorMode == By.ID:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.ID, locator)))
        elif locatorMode == By.NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.NAME, locator)))
        elif locatorMode == By.XPATH:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.XPATH, locator)))
        elif locatorMode == By.CSS_SELECTOR:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, locator)))
        elif locatorMode == By.CLASS_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, locator)))
        elif locatorMode == By.LINK_TEXT:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        elif locatorMode == By.PARTIAL_LINK_TEXT:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,
                                                  locator)))
        elif locatorMode == By.TAG_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.visibility_of_element_located(
                    (By.TAG_NAME, locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_until_element_clickable(self, waitTime, locatorMode, locator):
        if locatorMode == By.ID:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.ID, locator)))
        elif locatorMode == By.NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.NAME, locator)))
        elif locatorMode == By.XPATH:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.XPATH, locator)))
        elif locatorMode == By.CSS_SELECTOR:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator)))
        elif locatorMode == By.CLASS_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, locator)))
        elif locatorMode == By.LINK_TEXT:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, locator)))
        elif locatorMode == By.PARTIAL_LINK_TEXT:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.PARTIAL_LINK_TEXT, locator)))
        elif locatorMode == By.TAG_NAME:
            element = WebDriverWait(
                self.driver, waitTime).until(
                EC.element_to_be_clickable(
                    (By.TAG_NAME, locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def switch_to_window(self, windowHandle):
        self.driver.switch_to.window(windowHandle)

    def find_element(self, locatorMode, locator):
        if locatorMode == By.ID:
            element = self.driver.find_element_by_id(locator)
        elif locatorMode == By.NAME:
            element = self.driver.find_element_by_name(locator)
        elif locatorMode == By.XPATH:
            element = self.driver.find_element_by_xpath(locator)
        elif locatorMode == By.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(locator)
        elif locatorMode == By.CLASS_NAME:
            element = self.driver.find_element_by_class_name(locator)
        elif locatorMode == By.LINK_TEXT:
            element = self.driver.find_element_by_link_text(locator)
        elif locatorMode == By.PARTIAL_LINK_TEXT:
            element = self.driver.find_element_by_partial_link_text(locator)
        elif locatorMode == By.TAG_NAME:
            element = self.driver.find_element_by_tag_name(locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locatorMode, locator, text):
        self.find_element(locatorMode, locator).clear()
        self.find_element(locatorMode, locator).send_keys(text)

    def choose_option_from_dropdown(self, locatorMode, locator, option):
        dropdown_list = Select(self.find_element(locatorMode, locator))
        dropdown_list.select_by_visible_text(option)

    def click(self, waitTime, locatorMode, locator):
        self.wait_until_element_clickable(
            waitTime, locatorMode, locator).click()


class IncorrectPageException(Exception):
    """ This exception should be thrown when trying to instantiate the wrong
    page. """
