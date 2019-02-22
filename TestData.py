from faker import Faker


class TestData():
    """ Contains data which doesn't need to be changed overtime when running tests with different scenarions """
    VALID_USERNAME = "lepka1"
    VALID_PASSWORD = 'Lepka1234!'
    INVALID_USERNAME = 'FalseName'
    INVALID_PASSWORD = 'WrongPass'
    VALID_EMAIL = 'lepka1@o2.pl'
    INVALID_EMAIL = 'catmousergmail.com'
    COUNTRY = "United States"
    VALID_MESSAGE_HEADER = 'Webmaster'
    INVALID_MESSAGE_HEADER = 'Invalid'
    VALID_ORDER_REFERENCE = '1000'
    INVALID_ORDER_REFERENCE = 'dog'
    VALID_ATTACHMENT_PATH = '/home/beard/GithubRepos/SeleniumAutomationTests/test.txt'
    INVALID_ATTACHMENT_PATH = '/home/beard'


class DataGenerator():
    """ Uses faker library to generate random data used for various tests """

    def __init__(self):
        self.fake = Faker()
        self.generate_new_data()

    def generate_new_data(self):
        self.FIRST_NAME = self.fake.first_name()
        self.LAST_NAME = self.fake.last_name()
        self.ADDRESS_STREET = self.fake.street_name()
        self.ADDRESS_BUILDING = self.fake.secondary_address()
        self.CITY = self.fake.city()
        self.STATE = self.fake.state()
        self.ALIAS = self.fake.first_name()
        self.COMPANY = self.fake.company()
        self.POSTAL_CODE = self.fake.postalcode()
        self.PHONE_NUMBER = self.fake.phone_number()
        self.RANDOM_EMAIL = self.fake.email()
        self.RANDOM_PASSWORD = self.fake.password()
        self.PHONE_NUMBER = self.fake.msisdn()
