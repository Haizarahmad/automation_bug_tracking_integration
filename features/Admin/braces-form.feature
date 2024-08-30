Feature: Public User able to apply Braces Application

  @TS_03
  Scenario: Verify submitted form data matches displayed data
    Given url http://127.0.0.1:8000/booking_process
    And fill form with
      | field_attr_name| value      |
      | fullname       | John Doe   |
      | gender         | Male       |
      | address        | SL/51 Lorong Cahya Damai 7B3D, Taman Cahya Putri |
      | ic             | 021109130443                                     |
      | religion       | Islam                                            |
      | race           | Malay                                            |
    When click name btn-submit
    #Then The displayed data should match the submitted form data




