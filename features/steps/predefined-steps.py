from behave import *

@given('url {link}')
def go_to_page(context, link):
    context.driver.get(link)

@step('click {attr_type} {attr_name}')
def click_by_attribute(context, attr_type, attr_name):
    context.helper.click_element(attr_type, attr_name)

@step('fill {attr_type} {attr_name} {value}')
def input_by_attribute(context, attr_type, attr_name, value):
    context.helper.enter_text(attr_type, attr_name, value)

@step('fill form with')
def fill_form(context):
    for row in context.table:
        field_attr_name = row['field_attr_name']
        value = row['value']

        target_input_field = context.helper.find_element('name', field_attr_name)
        target_input_field.send_keys(value)



