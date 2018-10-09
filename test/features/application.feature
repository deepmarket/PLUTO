# Created by sgomena at 9/26/18

Feature: High level application testing
  # Enter feature description here

  Scenario Outline: Verify the application stands up
    When I stand up the application
      And I wait 2 seconds
      And I click on the <tab> tab
    Then the current tab should be the <tab> tab

    Examples:
      | tab       |
      | dashboard |
      | resources |
      | jobs      |