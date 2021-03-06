import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from ..TestData import DataGenerator

# Fixture for browsers


@pytest.yield_fixture(params=["firefox", "chrome"], autouse=True)
def driver_init(request, setUp_test_information_for_zelenium):
    selenium_hub_url = 'http://localhost:4444/wd/hub'
    capabilities = None
    options = None
    if request.param == "firefox":
        capabilities = DesiredCapabilities.FIREFOX
        options = webdriver.FirefoxOptions()
    elif request.param == "chrome":
        capabilities = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
    else:
        raise Exception(
            'Browser could not be specified\n Check test params !')

    capabilities['name'] = setUp_test_information_for_zelenium
    capabilities['idleTimeout'] = 90
    capabilities['recordVideo'] = False
    capabilities['testFileNameTemplate'] = "{testName}_{platform}_{browser}_{testStatus}"
    web_driver = webdriver.Remote(selenium_hub_url, capabilities,None,None,False,None,options) 
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def setUp_test_information_for_zelenium(request):
    return request.param


@pytest.yield_fixture
def data_generator():
    generator = DataGenerator()
    generator.generate_new_data()
    yield generator
