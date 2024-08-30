from behave import *

@given('I go to braces module')
def application_module(context):
    context.driver.get("http://127.0.0.1:8000/admin/application/braces")