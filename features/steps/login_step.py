from behave import *
from selenium import webdriver
from features.pages.login import LoginPages
from features.pages.dashboard import DashboardPages

@given(u'I launch to Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.implicitly_wait(20)

@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(*LoginPages.USERNAME).send_keys(user)
    context.driver.find_element(*LoginPages.PASSWORD).send_keys(pwd)


@when(u'Click in login button')
def step_impl(context):
    context.driver.find_element(*LoginPages.LOGIN_BUTTON).click()

@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(*DashboardPages.DASHBOARD_LABEL).text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"