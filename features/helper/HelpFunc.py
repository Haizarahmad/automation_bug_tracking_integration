from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time

#utility methods

class SeleniumHelper:
    def __init__(self, driver):  # Corrected __init__ method
        self.driver = driver

    #find element using xpath
    def is_element_present(self, value):
        try:
            element = self.driver.find_element(By.XPATH, value)
            if element.is_displayed():
                return element
        except NoSuchElementException:
            raise AssertionError("Element is not present")

    def page_wait(self):
        time.sleep(1)

    def get_text_from_alert(self):
        alert = Alert(self.driver)
        return alert.text

    def accept_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    def find_element(self, attr, attr_name):
        try:
            locator_strategy = {
                'id': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH
            }
            by = locator_strategy.get(attr.lower())

            return self.driver.find_element(by, attr_name)
        except NoSuchElementException:
            raise AssertionError("Element is not present")

        # locator_strategy = {
        #     'id': By.ID,
        #     'name': By.NAME,
        #     'xpath': By.XPATH
        # }
        # by = locator_strategy.get(attr.lower())
        #
        # #throw exception
        # if not by:
        #     raise ValueError(f"Unable to find element: {attr}")
        # return self.driver.find_element(by, attr_name)

    def click_element(self, attr, attr_name):
        element = self.find_element(attr, attr_name)
        element.click()


    # def find_element_by_id(self, id):
    #     return self.driver.find_element(By.ID, id)
    #
    # def find_element_by_name(self, name):
    #     return self.driver.find_element(By.NAME, name)

    def find_element_by_name_text(self, name):
        try:
            element = self.driver.find_element(By.NAME, name)
            value = element.get_attribute('value').strip()  # Use 'value' attribute instead of text

            if not value:
                print(f"Element with name '{name}' found but contains no value.")
                return None

            return value
        except NoSuchElementException:
            raise AssertionError(f"Element with name '{name}' not found")

    # def find_element_by_xpath(self, xpath):
    #     return self.driver.find_element(By.XPATH, xpath)

    # def find_element_by_linktext(self, linktext):
    #     return self.driver.find_element(By.LINK_TEXT, linktext)

    # def click_element_by_id(self, id):
    #     element = self.find_element_by_id(id)
    #     element.click()
    #
    # def click_element_by_xpath(self, xpath):
    #     element = self.find_element_by_xpath(xpath)
    #     element.click()
    #
    # def click_element_by_name(self, name):
    #     element = self.find_element_by_name(name)
    #     element.click()

    def enter_text(self, attr, attr_name, value):
        element = self.find_element(attr, attr_name)
        element.clear()
        element.send_keys(value)

    # def enter_text_by_name(self, name, text):
    #     element = self.find_element_by_name(name)
    #     element.send_keys(text)
    #
    # def enter_text_by_id(self, name, text):
    #     element = self.find_element_by_id(name)
    #     element.send_keys(text)
    #
    # def enter_text_by_xpath(self, name, text):
    #     element = self.find_element_by_xpath(name)
    #     element.send_keys(text)

