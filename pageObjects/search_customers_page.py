from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchCustomer:

    #constructor
    def __init__(self,driver: WebDriver):

        self.driver = driver

        # locators
        self.email_field = (By.XPATH,"//input[@id='SearchEmail']")
        self.fname_field = (By.XPATH,"//input[@id='SearchFirstName']")
        self.lname_field = (By.XPATH,"//input[@id='SearchLastName']")
        self.search_btn = (By.XPATH,"//button[@id='search-customers']")

        self.comp_role_search = (By.XPATH, "//li[@title='Registered']")
        self.cross_icon_search = (By.XPATH, "//span[@role='presentation']")
        self.company_roles_search = (By.XPATH, "//ul[@id='select2-SelectedCustomerRoleIds-results']//li")

        self.row_count = (By.XPATH,"//table[@id='customers-grid']//tbody//tr")
        self.col_count = (By.XPATH,"//table[@id='customers-grid']//tbody//tr//td")

    #Action Methods

    def enterEmail(self,email_id):
        self.driver.find_element(*self.email_field).send_keys(email_id)

    def enterFname(self,first_name):
        self.driver.find_element(*self.fname_field).send_keys(first_name)

    def enterLname(self,last_name):
        self.driver.find_element(*self.lname_field).send_keys(last_name)


    def select_customer_role_search(self,cus_role):
        wait = WebDriverWait(self.driver,10)

        customer_role = wait.until(expected_conditions.visibility_of_element_located(self.comp_role_search)).get_attribute("title")

        if customer_role != cus_role:
            self.driver.find_element(*self.cross_icon_search).click()
            customer_roles = wait.until(expected_conditions.visibility_of_element_located(self.company_roles_search)).find_elements(*self.company_roles_search)
            for role in customer_roles:
                if role.text == cus_role:
                    role.click()

    def getRowsCount(self):
        return len(self.driver.find_elements(*self.row_count))

    def getColsCount(self):
        return len(self.driver.find_elements(*self.col_count))

    def checkNameEmail(self,email,name=''):
        flag = False
        rows = self.getRowsCount()

        for i in range(1,rows+1):
            email_id = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(i)+"]//td[2]").text

            cus_name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(i)+"]//td[3]").text
            print(email_id)

            if email_id == email or cus_name == name:
                flag = True
                break

        return flag

    def clickSearchBtn(self):
        self.driver.find_element(*self.search_btn).click()