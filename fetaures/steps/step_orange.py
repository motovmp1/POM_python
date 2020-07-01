from behave import *
from selenium import webdriver
import time


@given('Launch Chrome Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    context.driver.implicitly_wait(20)
    context.driver.maximize_window()
    time.sleep(2)


@when('Open orange homepage')
def open_home(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    time.sleep(2)


@then('verify the logo present')
def logo_is_present(context):
    time.sleep(2)


@then('close navigator')
def close_navigator(context):
    time.sleep(3)
    context.driver.close()
