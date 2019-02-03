from .BaseTestCase import BaseTestClass
from ..pages.ContactPage import ContactPage
from SeleniumAutomationTests.TestData import Test_Data
from ..LocatorModes import LocatorMode


class ContactPageTests(BaseTestClass):

    def setUp(self):
        super(ContactPageTests, self).setUp()
        self.navigate_to_page(
            'http://automationpractice.com/index.php?controller=contact')

    def test_SendMessage(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.sendMessage(
            Test_Data['Valid_Message_header'], Test_Data['Valid_Email'],
            '1234', 'test message')
        pop_up_element = contact_page_obj.find_element(
            LocatorMode.CLASS_NAME, 'alert.alert-success')

        assert pop_up_element.text == 'Your ' \
            'message has been successfully sent to our team.'

    def tearDown(self):
        super().tearDown()
