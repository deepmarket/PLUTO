# Created by sgomena at 9/26/18

Feature: High level application testing
  # Enter feature description here

  Scenario: Verify the application stands up
#    When I wait 2 seconds
    When I stand up the application
#      And I wait 2 seconds
      And I click on the resources tab
#      And I execute the application
    Then the current tab should be the resources tab