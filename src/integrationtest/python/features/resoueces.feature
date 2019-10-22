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
    
  Scenario: Click on Cancel Button
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I click on the Cancel button
    Then the window will switch to controller page

  Scenario: Click on Next Button
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I click on the Next button
    Then the planning hint text should be "Please enter a machine name."

  Scenario: Enter machine configuration 
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "test machine" in the machine name input box
      And I enter "1" in the GPUs input box
      And I enter "1" in the Cores input box
      And I enter "1" in the RAM input box
    Then the machine name input box text should be "test machine"
      And the GPUs input box text should be "1"
      And the Cores input box text should be "1"
      And the RAM input box text should be "1"

  Scenario: No machine name input
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "1" in the GPUs input box
      And I enter "1" in the Cores input box
      And I enter "1" in the RAM input box
      And I click on the Next button
    Then the planning hint text should be "Please enter a machine name."

  Scenario: No GPUs input
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "test machine" in the machine name input box
      And I enter "1" in the Cores input box
      And I enter "1" in the RAM input box
      And I click on the Next button
    Then the planning hint text should be "Please enter number of GPUs."

  Scenario: No Cores input
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "test machine" in the machine name input box
      And I enter "1" in the GPUs input box
      And I enter "1" in the RAM input box
      And I click on the Next button
    Then the planning hint text should be "Please enter number of cores."


  Scenario: No RAM input
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "test machine" in the machine name input box
      And I enter "1" in the GPUs input box
      And I enter "1" in the Cores input box
      And I click on the Next button
    Then the planning hint text should be "Please enter number of RAM."
