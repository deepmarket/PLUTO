# Created by sgomena at 9/26/18

Feature: High level application testing
  # Enter feature description here

  Scenario: Enter login credentials
    When I spin up the application
      And I open the login dialog
      And I enter "samgomena@gmail.com" in the username input box
#      And I wait 5 seconds
      And I enter "password" in the password input box
    Then the username input box text should be "samgomena@gmail.com"
      And the password input box text should be "password"

  Scenario: Verify no input hint
    When I spin up the application
      And I open the login dialog
      And I click the login button
    Then the login hint text should be "Please enter your email and password."

  Scenario: Verify only email input hint
    When I spin up the application
      And I open the login dialog
      And I enter "test_user@test_email.com" in the username input box
      And I click the login button
    Then the login hint text should be "Please enter your password."

  Scenario: Verify only password input hint
    When I spin up the application
      And I open the login dialog
      And I enter "test_password" in the password input box
      And I click the login button
    Then the login hint text should be "Please enter your email."

  Scenario: Verify incorrect credentials hint
    When I spin up the application
      And I open the login dialog
      And I enter "test_user@test_email.com" in the username input box
      And I enter "test_password" in the password input box
      And I click the login button
    Then the login hint text should be "The email or password you entered is invalid."

  Scenario: Verify incorrect credentials hint
    When I spin up the application
      And I open the login dialog
      And I enter "samgomena@gmail.com" in the username input box
      And I enter "password" in the password input box
      And I click the login button
    Then I should be able to log in to the application

#  Scenario Outline: Verify the application stands up
#    When I stand up the application
#      And I wait 2 seconds
#      And I click on the <tab> tab
#    Then the current tab should be the <tab> tab
#
#    Examples:
#      | tab       |
#      | dashboard |
#      | resources |
#      | jobs      |