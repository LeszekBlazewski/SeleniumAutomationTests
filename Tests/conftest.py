import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


# Fixture for browsers
@pytest.yield_fixture(params=["firefox", "chrome"], autouse=True)
def driver_init(request, setUp_test_information_for_zelenium):
    selenium_hub_url = 'http://localhost:4444/wd/hub'
    capabilities = None
    if request.param == "firefox":
        capabilities = DesiredCapabilities.FIREFOX
    elif request.param == "chrome":
        capabilities = DesiredCapabilities.CHROME
    else:
        raise Exception(
            'Browser could not be specified\n Check test params !')

    capabilities['name'] = setUp_test_information_for_zelenium
    capabilities['idleTimeout'] = 90
    capabilities['recordVideo'] = False
    capabilities['testFileNameTemplate'] = "{testName}_{platform}_{browser}_{testStatus}"
    web_driver = webdriver.Remote(selenium_hub_url, capabilities)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def setUp_test_information_for_zelenium(request):
    return request.param
