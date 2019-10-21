# Created by Fenting Lin on 10/14/19

Feature: # Verify functionality on resources tab
   # This inlcueds everything from clicking on the resources tab

  Scenario Outline: Verify the application stands up
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
    Then the current tab should be the resources tab

  Scenario: Click on Add Button
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
    Then the window will switch to add resource page
    
