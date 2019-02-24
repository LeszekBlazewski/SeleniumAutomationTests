# SeleniumAutomationTests

This repository is a  simple automation framework written  for practice purposes.

## Background

I have always been interested in automated testing, QA and automating the workflow of different tasks. This repository is my little project that I have developed during my free time while studying computer science.

## Main target

Main purpose of this repository is to showcase different patterns, technologies and use of frameworks which I have learned overtime while writing this automation library using selenium and python.

I have chosen this [page](http://automationpractice.com/index.php) as my main target against which I would run my UI end to end tests.

## How can I test it out ?

### **Requirements**

First you need to make sure that you possess all of the required dependencies and plugins.

#### 1. Install  docker & docker-compose if you don't possess this awesome tools.

#### 2. Clone the repository

```bash
git clone https://github.com/LeszekBlazewski/SeleniumAutomationTests.git && cd SeleniumAutomationTests
```

#### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### **Example usage**

#### 1. Create your test environment by spinning up docker containers

```bash
docker-compose up -d
```

#### 2. Take advantage of pytest to run your tests

First navigate to the Tests folder and from there execute your tests using pytest as shown below.

Example command to run all tests inside [`LoginPageTests.py`](\Tests\LoginPageTests.py) module in parallel by using 6 threads.

```bash
py.test LoginPageTests.py -n 6
```

**Quickly navigate to [live preview](http://localhost:4444/grid/admin/live) and see your tests running !**

**Don't forget to check out the tests result on the [dashboard](http://localhost:4444/dashboard) !**

## Description

This section contains a brief description and explanation of patterns and frameworks which I have used to develop this project.

### Selenium & python

The whole library is based on [selenium](https://www.seleniumhq.org/) which was also implemented as a library in python. Selenium provides an easy and straightforward way to interact with DOM therefore it allows automation of any task that a client could perform manually on web-page whatsoever.

#### Page object model

This pattern provides a level of abstraction between actual code and test cases. It keeps the test cases clear and understandable for everyone. POM is a natural way of representing each page as different object. Therefore test cases only require creation of specific objects on demand and running functions as needed which keeps the test cases stupidly simple as in KISS principle.

#### Selenium wrappers & abstraction of data

As you can see in [`BasePage.py`](\pages\BasePage.py) I have created my own wrappers for the selenium functions in order to speed up the development process and ensure that everything works as expected.

I have also abstracted selectors of each element into separate module where they are grouped in classes by page objects to which they correspond. This ensures that whenever a selector needs to be changed you only have to  modify [`Locators.py`](\Locators.py) file. The same goes for URLS.

#### FAKER

When running tests corresponding to login, registration flow etc. across many browsers a pretty big data set is required. I designed a special pytest fixture which creates test data on demand by using faker. This ensures that each test run won't fail because of the fact that user data has been already used - for example during registration process(you can't create two accounts with same email)

I highly recommend checking out the [FAKER github page](https://github.com/joke2k/faker) and [docs](https://faker.readthedocs.io/en/master/) for more references and information !

#### Pytest

Pytest is an awesome test framework implemented as a python module. It helps you define and run tests which fit all your needs.

I decided to used pytest because of

- [***Fixtures***](#fixtures-in-code-explanation)
- [***Parallel test execution***]((#2.-take-advantage-of-pytest-to-run-your-tests))
- [***Convenient way to provide data to tests***](#generate-new-test-data-on-demand)
- ***Multiple runs of test cases***
- ***Endless possibilities of settings customization***

For more information about the framework checkout the pytests [documentation](https://docs.pytest.org/en/latest/).

##### Fixtures in code explanation

Pytest provides a really convenient way to inject test data, common objects for tests and so forth as shown below.

##### Creating webdriver instance based on fixture parameter

```python
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
```

When we want to run tests against different browsers we only have to add a parameter in the header and change the function respectively to properly create webdriver instance. The autouse parameter ensures that this fixture will be used for each test case. It can be accessed within the test function after injection by accessing the driver_init parameter.

##### Generate new test data on demand

Another simple example which shows how handy fixtures can be. Example shown below creates new instance of [`DataGenerator`](TestData.py) which uses faker in order to produce data and stores it within the newly created object.

```python
@pytest.yield_fixture
def data_generator():
    generator = DataGenerator()
    generator.generate_new_data()
    yield generator
```

Whenever a test case needs new data we simply inject this fixture and then access it within the test function.

## Test environment

### Main requirements for the environment

Everyone who has interest in QA knows that websites need to be tested across many platforms and different browsers. Selenium provides perfect solution to this problem by setting up a grid and connection nodes to it but it still takes much time to accomplish all of this tasks.

**Docker to the rescue !**

### Why docker ?

Because of the simplicity and level of abstraction it provides. You can run your tests against different browsers without even having any browser installed ! Selenium gird and nodes can be run inside docker containers which allows automatic setup of the test environment and orchestration on a whole new level. When using docker the process of running tests can be automatically scaled to perform even faster.

### Zalenium

Zalenium is a flexible and scalable container based Selenium Grid which contains a bunch of useful tools which will speed up the testing process.

The best part about Zalenium is that the whole project is open source and it works out of the box in docker !

You should definitely check out the zalenium [project page](https://opensource.zalando.com/zalenium/) and [github repository](https://github.com/zalando/zalenium) for further information and more in depth descriptions.

#### Zalenium goodies

Some of the tools that I took advantage of while creating this small project:

1. Automatic scaling of the containers and nodes creaction
2. Live preview of the tests
3. Interaction via VNC with the browsers
4. Test run video footage
5. Dashboard which provides comprehensive information about tests
6. Automatic logs creation which contain all of the necessary data about tests

You can observe in code that I am referring to some of the Zalenium specific functions such as below

```python
driver_init.add_cookie(cookies[1])
```

By using cookies we specify whether given test will be displayed as successful or not in the dashboard. By default I mark every test case as failure and after assertions we set it to be successful.

## Contributing

Pull requests are welcome !

I am always open for any suggestions and critics.

For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](LICENSE)