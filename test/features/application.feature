# Created by sgomena at 9/26/18

Feature: High level application testing
  # Enter feature description here

  Scenario Outline: Verify the application stands up
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I wait 1 second
      And I click on the <tab> tab
    Then the current tab should be the <tab> tab

    Examples:
      | tab       |
      | dashboard |
      | resources |
      | jobs      |