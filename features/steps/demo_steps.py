from behave import given, then

@then("User verifies home page")
def step_impl(context):
    element = context.home_page.wait_for_home_page()
    assert element.is_displayed()