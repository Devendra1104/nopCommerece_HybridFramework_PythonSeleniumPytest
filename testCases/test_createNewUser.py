import pytest

from pageObjects.loginPageAdmin import LoginPageAdmin
from pageObjects.addCustomerPage import AddCustomerPage
from utilities.getProperties import GetProperties
from utilities.loggerUtility import LoggerUtility


class TestCreateNewUser:

    @pytest.mark.sanity
    def test_add_customer(self,setDriver):

        driver = setDriver

        login = LoginPageAdmin(driver)
        login.enterEmail(GetProperties.getID())
        login.enterPassword(GetProperties.getPassword())
        login.clickLoginCTA()

        add_customer = AddCustomerPage(driver)
        add_customer.navigate_to_form()
        add_customer.enter_email("xyz@gmail.com")
        add_customer.enter_fname("Jack")
        add_customer.enter_lname("Sparrow")
        add_customer.select_customer_role("Registered")
        add_customer.choose_manager("Vendor 2")
        add_customer.click_save()

        if add_customer.success_message() == "The new customer has been added successfully.":
            assert True


