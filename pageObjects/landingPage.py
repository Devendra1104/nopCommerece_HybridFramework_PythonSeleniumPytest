from selenium.webdriver.common.by import By

class LandingPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver
        # locators
        self.loginCTA = (By.XPATH,"//a[normalize-space()='Log in']")

    # actionMethods
    def clickLogin(self):
        self.driver.find_element(*self.loginCTA).click()
