import pytest

from pageObjects.loginPageAdmin import LoginPageAdmin
from pageObjects.search_customers_page import SearchCustomer
from pageObjects.addCustomerPage import AddCustomerPage
from utilities.getProperties import GetProperties

class TestSearchUser:

    @pytest.mark.regression
    def test_searchUser(self,setDriver):

        driver = setDriver

        login = LoginPageAdmin(driver)
        login.enterEmail(GetProperties.getID())
        login.enterPassword(GetProperties.getPassword())
        login.clickLoginCTA()

        addCustomer = AddCustomerPage(driver)
        addCustomer.navigate_to_search()

        searchCustomer = SearchCustomer(driver)
        searchCustomer.enterEmail("abc@gmail.com")
        searchCustomer.select_customer_role_search("Registered")
        searchCustomer.clickSearchBtn()

        status = searchCustomer.checkNameEmail("abc@gmail.com")

        if status:
            assert True

        else:

            assert False









