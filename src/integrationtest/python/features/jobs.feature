# Created by Fenting Lin on 10/23/19

Feature: # Verify functionality on jobs tab
   # This inlcueds everything from clicking on the jobs tab

  Scenario Outline: Verify the application stands up
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the jobs tab
    Then the current tab should be the jobs tab
