from Mantis.log_Issue import MantisLogIssue
from helper.HelpFunc import SeleniumHelper
from selenium import webdriver
from datetime import datetime
import csv

def before_all(context):
    # Initialize a list to track scenario results
    context.new_issue = MantisLogIssue()
    context.steps_results = []

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.helper = SeleniumHelper(context.driver)
    context.current_scenario = scenario.name

def after_step(context, step):
    context.steps_results.append({
        "scenario": context.current_scenario,
        "name": step.name,
        "status": step.status,
        "exception": step.exception  # Ensure exception is converted to string
    })

    # Log issue if step fails
    # Uncomment if needed
    # if step.status == "failed":
    #     context.new_issue.log_issue(f"Step failed: {step.name}", f"{step.exception}")

    # Add a wait after each step
    context.helper.page_wait()

def after_scenario(context, scenario):
    context.driver.quit()

# def after_all(context):
#     # Specify the file path for the CSV report
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     report_filename = f"Test_Report_{timestamp}.csv"
#
#     # Write the results to a CSV file
#     with open(report_filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         headers = ["Scenario","Step Name", "Status", "Exception"]
#         writer.writerow(headers)
#         for result in context.steps_results:
#             row = [result["scenario"],result["name"], result["status"], result["exception"]]
#             writer.writerow(row)
