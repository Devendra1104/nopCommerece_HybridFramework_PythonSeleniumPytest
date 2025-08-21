import pytest
from selenium import webdriver
from utilities.getProperties import GetProperties

@pytest.fixture()
def setDriver(browser):

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.get(GetProperties.getURL())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    driver.close()

#This method adds options which we can use or add via CLI

def pytest_addoption(parser):
    parser.addoption("--browser",default = "chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
