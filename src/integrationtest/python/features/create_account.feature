# Created by sgomena at 6/20/19
Feature: Verify account creation

  Scenario: Enter New Account Credentials
    Given the user is logged out of the application
    When I spin up the application
      And I open the login window
