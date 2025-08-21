import pytest

from pageObjects.landingPage import LandingPage
from pageObjects.loginPage import LoginPage
from pageObjects.loginPageAdmin import LoginPageAdmin
from utilities.getProperties import GetProperties
from utilities.loggerUtility import LoggerUtility


logger = LoggerUtility.loggen()

class TestLogin:

    @pytest.mark.sanity
    def test_pageTitle(self,setDriver):

        logger.info("*************Test Page title started*******************")
        self.driver = setDriver
        page_title = self.driver.title

        if page_title == "nopCommerce demo store. Login":
            logger.info("*************Test Page title passed*******************")
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\test_pageTitle.png")
            logger.info("*************Test Page title failed *******************")
            assert False


    @pytest.mark.regression
    def test_login(self, setDriver):

        self.driver = setDriver
        logger.info("*************Test login started*******************")
        lp = LandingPage(self.driver)
        lp.clickLogin()

        login = LoginPage(self.driver)
        login.enterEmail(GetProperties.getID())
        logger.info("*************Entered ID*******************")
        login.enterPassword(GetProperties.getPassword())
        logger.info("*************Entered password*******************")
        login.clickLoginCTA()
        logger.info("*************Clicked Login*******************")

        self.message = login.welcomeMsg()
        print(self.message)

        if self.message == "Welcome to our store":
            logger.info("*************Login Passed*******************")
            assert True

        else:

            self.driver.save_screenshot(".\\screenshots\\"+"testLoginMessage.png")
            logger.info("*************Login Failed*******************")
            assert False











