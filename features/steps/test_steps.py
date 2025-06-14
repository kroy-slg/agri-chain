from behave import given, when, then
from features.pages.home_page import HomePage
from features.pages.result_page import ResultPage

@given("User open agri chain home page")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open()

@when('User enters "{text}" into the input field')
def step_impl(context, text):
    context.home_page.enter_input(text)

@when("User enters a large input string")
def step_impl(context):
    large_input = "This is large string" * 100
    context.home_page.enter_input(large_input)

@when("User clicks the submit button")
def step_impl(context):
    context.home_page.click_submit()

@then('User should see the output "{expected_output}"')
def step_impl(context, expected_output):
    result_page = ResultPage(context.driver)
    actual = result_page.get_output()
    assert actual == expected_output
