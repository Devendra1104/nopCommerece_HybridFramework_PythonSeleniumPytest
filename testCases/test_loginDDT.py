from pageObjects.loginPageAdmin import LoginPageAdmin
from utilities.getProperties import GetProperties
from utilities.loggerUtility import LoggerUtility
from utilities import ExcelUtil

logger = LoggerUtility.loggen()

class TestLoginDDT:

    def test_loginDDT(self,setDriver):

        file_path = "C://Users//deven//PythonTesting//HybridTestFramework//testData//loginTestData.xlsx"
        rows = ExcelUtil.getRowCount(file_path, "Sheet2")
        self.driver = setDriver
        admin_login = LoginPageAdmin(self.driver)

        for r in range(2,rows+1):
            id = ExcelUtil.readData(file_path,"Sheet2",r,1)
            password = ExcelUtil.readData(file_path, "Sheet2", r, 2)
            exp_res = ExcelUtil.readData(file_path, "Sheet2", r, 3)

            admin_login.enterEmail(emailId=id)
            admin_login.enterPassword(password=password)
            admin_login.clickLoginCTA()

            act_title = self.driver.title

            if act_title == "Dashboard / nopCommerce administration":
                if exp_res == "valid":
                    print("Login Success with valid Creds")
                    ExcelUtil.writeData(file_path,"Sheet2",r,4,"Pass")
                    admin_login.clickLogoutCTA()

                    assert True

                elif exp_res == "invalid":
                    print(" Login Failed with valid creds.")
                    ExcelUtil.writeData(file_path, "Sheet2", r, 4, "Fail")
                    admin_login.clickLogoutCTA()

                    assert False


            elif act_title != "Dashboard / nopCommerce administration":
                if exp_res == "valid":
                    print("Login Failed with Valid creds")
                    ExcelUtil.writeData(file_path, "Sheet2", r, 4, "Fail")
                    admin_login.clickLogoutCTA()

                    assert False

                elif exp_res == "invalid":
                    print("Login failed with invalid creds")
                    ExcelUtil.writeData(file_path, "Sheet2", r, 4, "Pass")

                    assert True








