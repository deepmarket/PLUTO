# Created by Fenting Lin on 10/14/19

Feature: # Verify functionality on resources tab
   # This inlcueds everything from clicking on the resources tab

  Scenario: Click on Resources tab
    When I click on the Resources tab
    Then the window will switch to resources page

  Scenario: Click on Add Button
    When I click on the Resources tab
      And I click on the Add button
    Then the window will switch to add resource page

  Scenario: Verify no input hint
    When I click on the Resources tab
      And I click on the Add button
      And I click on the Submit button