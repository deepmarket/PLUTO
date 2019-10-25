# Created by sgomena at 10/24/19
Feature: Verify Functionality Around Settings
  # Enter feature description here

  Scenario: Settings List View
    Given the user is logged out of the application
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I click the login button
      And I open the application window
      And I click on the settings tab
    Then the current tab should be the settings tab
    Then the current view should be the workspace view
