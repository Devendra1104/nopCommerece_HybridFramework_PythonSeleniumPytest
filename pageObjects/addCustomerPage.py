from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class AddCustomerPage:

    #locators

    customer_link_sidebar = (By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    customer_sub_link_sidebar = (By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    add_new_btn = (By.XPATH,"//a[@class='btn btn-primary']")

    email_text = (By.XPATH,"//input[@id='Email']")
    pass_text = (By.XPATH,"//input[@id='Password']")
    fname_text = (By.XPATH,"//input[@id='FirstName']")
    lname_text = (By.XPATH,"//input[@id='LastName']")
    male_rd_btn = (By.XPATH,"//input[@id='Gender_Male']")
    female_rd_btn = (By.XPATH,"//input[@id='Gender_Female']")
    company_name_text = (By.XPATH,"//input[@id='Company']")
    tax_ex_chbox = (By.XPATH,"//input[@id='IsTaxExempt']")
    news_letter = (By.XPATH,"//span[@aria-expanded='true']//input[@role='searchbox']")

    company_role_tex = (By.XPATH,"//li[@title='Registered']")
    cross_icon = (By.XPATH,"//span[@role='presentation']")
    company_roles = (By.XPATH,"//ul[@id='select2-SelectedCustomerRoleIds-results']//li")


    vendor_manager = (By.XPATH,"//select[@id='VendorId']")
    active_chbox = (By.XPATH,"//input[@id='Active']")
    changepass_chbox = (By.XPATH,"//input[@id='MustChangePassword']")
    admin_comment_txt = (By.XPATH,"//textarea[@id='AdminComment']")
    save_btn = (By.XPATH,"//button[@name='save']")

    success_msg = (By.XPATH,"//div[@class='alert alert-success alert-dismissable']")

    #constructor
    def __init__(self,driver: WebDriver):
        self.driver = driver

    #ActionMethods

    def navigate_to_form(self):
        self.driver.find_element(*self.customer_link_sidebar).click()
        self.driver.find_element(*self.customer_sub_link_sidebar).click()
        self.driver.find_element(*self.add_new_btn).click()

    def navigate_to_search(self):
        self.driver.find_element(*self.customer_link_sidebar).click()
        self.driver.find_element(*self.customer_sub_link_sidebar).click()

    def enter_email(self,email):
        self.driver.find_element(*self.email_text).send_keys(email)

    def enter_fname(self,fname):
        self.driver.find_element(*self.fname_text).send_keys(fname)

    def enter_lname(self,lname):
        self.driver.find_element(*self.lname_text).send_keys(lname)


    def select_customer_role(self,cus_role):
        wait = WebDriverWait(self.driver,10)

        customer_role = wait.until(expected_conditions.visibility_of_element_located(self.company_role_tex)).get_attribute("title")

        if customer_role == "Registered":
            self.driver.find_element(*self.cross_icon).click()

        customer_roles = wait.until(expected_conditions.visibility_of_element_located(self.company_roles)).find_elements(*self.company_roles)

        for role in customer_roles:
            if role.text == cus_role:
                role.click()

    def choose_manager(self,vendor_name):
        managers = Select(self.driver.find_element(*self.vendor_manager))
        managers.select_by_visible_text(vendor_name)

    def click_save(self):
        self.driver.find_element(*self.save_btn).click()

    def success_message(self):
        return self.driver.find_element(*self.success_msg).text

