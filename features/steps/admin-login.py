from behave import *

@given('Positive login credentials test data for admin')
@given('Negative login credentials test data for admin')
def enter_login_credentials(context):
    for row in context.table:
        context.helper.enter_text('name', 'username', row['username'])
        context.helper.enter_text('name', 'password', row['password'])

@then('Login failed present')
def check_failed_message(context):
    context.helper.is_element_present('//div[text()="Login faile"]')

# Execute steps in step
@given('I login as admin')
def login_as_admin(context):
    context.execute_steps(u"""
        Given Positive login credentials test data for admin
         |username||password|
         |Haizar||haizar1234|
        Then I click login button
    """)


