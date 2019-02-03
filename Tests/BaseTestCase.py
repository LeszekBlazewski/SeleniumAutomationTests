from selenium import webdriver
from ..DriverSettings import Driver_Settings
import unittest


class BaseTestClass(unittest.TestCase):
    """Contains the basic definition for all test cases in the project."""

    def setUp(self):
        """Prepares the driver with desired options based on the
        DriverSettings.py file."""
        browserName = Driver_Settings.get('Browser').lower()
        if browserName == 'firefox':
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('-headless')
            self.driver = webdriver.Firefox(options=self.options)
        elif browserName == 'chrome':
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Chrome(chrome_options=self.options)
        elif browserName == 'opera':
            self.options = webdriver.ChromeOptions()
            self.options.binary_location = r"C:\Program Files\Opera\launcher" \
                ".exe"
            self.driver = webdriver.Opera(options=self.options)
        if self.driver is not None:
            self.driver.maximize_window()
        else:
            raise Exception(
                'Browser could not be specified.\n '
                'Please check your DriverSettings.py file.')

    def navigate_to_page(self, url):
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
