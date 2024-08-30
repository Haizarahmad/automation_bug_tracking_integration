from behave import *

# Define the mapping between table headers and HTML fields
# Table header name : HTML name attribute
field_mapping = {
    'fullname': 'fullname',
    'gender': 'gender',
    'address': 'address',
    'NRIC': 'ic',
    'religion': 'religion',
    'race': 'race'
}

@given('Positive test data for Braces Application')
def enter_form_data(context):
    for row in context.table:
        for header, html_attr in field_mapping.items():
            context.helper.enter_text_by_name(html_attr, row[header])
            setattr(context, header, row[header])

@then('The displayed data should match the submitted form data')
def compare_data_braces(context):
    for header, html_attr in field_mapping.items():
        displayed_value = context.helper.find_element_by_name_text(html_attr)
        expected_value = getattr(context, header)
        assert expected_value == displayed_value, f"Expected {header.capitalize()}: {expected_value}, but got {displayed_value}"
