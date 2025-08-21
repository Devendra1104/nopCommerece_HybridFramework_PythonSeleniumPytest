from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class LoginPageAdmin:

    #constructor
    def __init__(self,driver: WebDriver):
        self.driver = driver

        # locators
        self.emailField = (By.XPATH,"//input[@id='Email']")
        self.passwordField = (By.XPATH,"//input[@id='Password']")
        self.loginButton = (By.XPATH,"//button[normalize-space()='Log in']")
        self.logoutButton = (By.XPATH,"//a[normalize-space()='Logout']")
        self.welcomeMessage = (By.XPATH,"//h2[normalize-space()='Welcome to our store']")

    #actionMethods

    def enterEmail(self,emailId):
        self.driver.find_element(*self.emailField).clear()
        self.driver.find_element(*self.emailField).send_keys(emailId)

    def enterPassword(self,password):
        self.driver.find_element(*self.passwordField).clear()
        self.driver.find_element(*self.passwordField).send_keys(password)

    def clickLoginCTA(self):
        self.driver.find_element(*self.loginButton).click()

    def clickLogoutCTA(self):
        self.driver.find_element(*self.logoutButton).click()

    def welcomeMsg(self):
        self.msg = self.driver.find_element(*self.welcomeMessage).text

        if self.msg:
            return self.msg

        else:
            return "invalid login"

