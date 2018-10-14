from pages.BasePage import BasePage, IncorrectPageException
from TestData import Test_Data


class ContactPage(BasePage):
    """Class represents the contact page."""

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(
                10, 'xpath', "//*[text()='Customer service - Contact us']")
        except BaseException:
            raise IncorrectPageException

    def submit_request(self):
        self.fill_out_field('id', 'email', Test_Data['Valid_Email'])
