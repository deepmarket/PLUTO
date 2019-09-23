# Created by Sam Gomena on 10/11/18

Feature: # Verify functionality around logging into the application
   # This includes everything from opening up the 'login' dialog up to just before the main 'application'
   # window opens.

  Scenario: Enter login credentials
    When I spin up the application
      And I open the login window
      And I enter "samgomena@gmail.com" in the username input box
      And I enter "password" in the password input box
    Then the username input box text should be "samgomena@gmail.com"
      And the password input box text should be "password"

  Scenario: Verify no input hint
    When I spin up the application
      And I open the login window
      And I click the login button
    Then the login hint text should be "Please enter your email and password."

  Scenario: Verify only email input hint
    When I spin up the application
      And I open the login window
      And I enter "test_user@test_email.com" in the username input box
      And I click the login button
    Then the login hint text should be "Please enter your password."

  Scenario: Verify only password input hint
    When I spin up the application
      And I open the login window
      And I enter "test_password" in the password input box
      And I click the login button
    Then the login hint text should be "Please enter your email."

  Scenario: Verify incorrect credentials hint
    When I spin up the application
      And I open the login window
      And I enter "test_user@test_email.com" in the username input box
      And I enter "test_password" in the password input box
      And I click the login button
    Then the login hint text should be "The email or password you entered is not recognized."

  Scenario: Verify correct credentials hint
    When I spin up the application
      And I open the login window
      And I enter "samgomena@gmail.com" in the username input box
      And I enter "password" in the password input box
      And I click the login button
    Then I should be able to log in to the application
