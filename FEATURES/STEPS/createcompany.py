from behave import given, when, then
from selenium.webdriver.support.select import Select
# from FEATURES.STEPS.Login import *
from selenium import webdriver

@given('user is on the Home page')
def homepg(context):
    txt = context.driver.current_url
    assert txt == "http://localhost:90/finsys/index.php#"
    context.driver.close()