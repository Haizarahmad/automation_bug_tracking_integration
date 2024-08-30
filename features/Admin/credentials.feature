Feature: Admin able to Login and Logout the system

  Background: #Run before every scenario
    Given url http://127.0.0.1:8000/login_page

  @TS_01
  Scenario: Admin login is successful
    Given fill form with
      | field_attr_name|  value      |
      | username       |  Haizar     |
      | password       |  haizar1234 |
    Then click name login-btn

  @TS_02
  Scenario: Admin login is unsuccessful
    Given Negative login credentials test data for admin
      |username||password|
      |admin||124|
    Then I click login button
    And Login failed present

