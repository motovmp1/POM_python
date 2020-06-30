import time
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.UserName_textbox_is = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_user_name(self, username):
        self.driver.find_element_by_id(self.UserName_textbox_is).clear()
        self.driver.find_element_by_id(self.UserName_textbox_is).send_keys(username)

    def enter_password_number(self, password):
        time.sleep(1)
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        time.sleep(1)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def login_button_press(self):
        self.driver.find_element_by_id("btnLogin").click()
