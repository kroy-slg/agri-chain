from behave import *

from features.pages.dashboard_page import DashboardPage
from features.pages.login_page import LoginPage

@when('User open orange hrm home page')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.wait_for_login_page()

@when('User enters username "{user}" and password "{password}"')
def step_impl(context, user, password):
    login_page = LoginPage(context.driver)
    login_page.enter_username(user)
    login_page.enter_password(password)

@when('User clicks login button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()

@then('User successfully login to dashboard page')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    page_ref = dashboard_page.get_dashboard_page()
    assert page_ref == "Dashboard"

@given("User open hrm login page")
def open_hrm_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()