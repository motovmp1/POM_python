from selenium import webdriver
import time
import unittest
import sys
# base_path = "C://Users/elsys/Documents/pycharm_robot/basic_python"
# sys.path.append(base_path)

from ..Login_page_POM import LoginPage
from ..Home_page import HomePage


class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        current_web_page = self.driver.current_url
        print(current_web_page)
        assert current_web_page == "https://opensource-demo.orangehrmlive.com/"

        login = LoginPage(driver)
        login.enter_user_name("Admin")
        time.sleep(1)
        login.enter_password_number("admin123")
        time.sleep(1)
        login.login_button_press()
        time.sleep(1)

        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(2)
        homepage.logout_button()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
