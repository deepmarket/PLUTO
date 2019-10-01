# Created by sgomena at 6/20/19
Feature: Verify account creation

  Scenario: Enter New Account Credentials
    When I spin up the application
      And I open the login window
      And I click the create an account button
