from behave import fixture,use_fixture, model
from selenium import webdriver
import os

def before_all(context):
    print(context)
    browsername=context.config.userdata['browser']
    if browsername=="ch":
       driver=webdriver.Chrome(context.config.userdata["ch_webdriver_exe"])
       context.driver=driver
    if browsername=="ie":
       driver=webdriver.Ie(context.config.userdata["ie_webdriver_exe"])
       context.driver=driver
    if browsername=="ff":
        driver = webdriver.Firefox(context.config.userdata["ff_webdriver_exe"])
        context.driver = driver
#comment

#Comment on Github
