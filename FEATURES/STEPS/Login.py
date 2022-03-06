from behave import given, when, then

from selenium import webdriver

@given('user opens the "{strURL}" url')
def OpenBrowser(context, strURL):
    context.driver = webdriver.Chrome("C:\\Webdrivers\Chromedriver.exe")
    print(strURL + " ####################")
    context.driver.get(strURL)


@given('user is on the application login page')
def applgpg(context):
    context.driver.find_element_by_xpath("//span//input[@type='password']").is_enabled()


@when('user enters "{user}" as username')
def enterusername(context, user):
    context.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(user)


@when('user enters "{passwd}" as password')
def enterpasswd(context, passwd):
    context.driver.find_element_by_xpath("//span//input[@type='password']").send_keys(passwd)


@when('user clicks on login button')
def loginclk(context):
    context.driver.find_element_by_xpath("//a[@href='#']").click()


@then('user is on the application home page')
def homepg(context):
    txt = context.driver.current_url
    assert txt == "http://localhost:90/finsys/index.php"
    # context.driver.close()


@then('user gets the message starting with "Welcome" on the top')
def welcome(context):
        print("Success")