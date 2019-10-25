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
    
  Scenario: Click on Cancel Button on the first page of add new resource
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I click on the Cancel button
    Then the window will switch to controller page

  Scenario: Click on Next Button Without Enter Anything
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

  Scenario Outline: Valid <config> input
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "1" in the <config> input box
    Then the <config> input box text should be "1"
      And the planning hint text should be ""
      And the <display> config box in machine configuration section should be Green

    Examples:
      | config | display |
      | GPUs   | Compute |
      | Cores  | Cores   |
      | RAM    | RAM     |

  Scenario Outline: Invalid <config> input
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the resources tab
      And I click on the Add button
      And I enter "10000" in the <config> input box
    Then the <config> input box text should be "10000"
      And the planning hint text should be <hint>
      And the <display> config box in machine configuration section should be Red

    Examples:
      | config | display | hint                              |
      | GPUs   | Compute | "Input for GPUs is out of range." |
      | Cores  | Cores   | "Cores is out of range."          |
      | RAM    | RAM     | "Amount of RAM is out of range."  |

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
      And I click on the Next button
    Then the window will switch to next page

  Scenario: Click on Back Button 
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
      And I click on the Next button
    Then the window will switch to next page
    When I click on the Back button
    Then the window will switch to add resource page
      And the machine name input box text should be "test machine"
      And the GPUs input box text should be "1"
      And the Compute config box in machine configuration section should be Green
      And the Cores input box text should be "1"
      And the Cores config box in machine configuration section should be Green
      And the RAM input box text should be "1"
      And the RAM config box in machine configuration section should be Green

  Scenario: Click on Cancel Button on the second page of add new resource
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
      And I click on the Next button
    Then the window will switch to next page
    When I click on the Cancel button
    Then the window will switch to controller page

  Scenario: Check attendance box default select
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
      And I click on the Next button
    Then the window will switch to next page
      And the attendance box current select is rent immediately box

  Scenario Outline: Check attendance box select
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
      And I click on the Next button
    Then the window will switch to next page
    When I click on the <box> button
    Then the attendance box current select is <box> box      

    Examples:
      | box              |
      | rent immediately |
      | rent schedule    |
      | rent reserve     |
  
  Scenario Outline: Check attendance box select <combo> select time
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
      And I click on the Next button
    Then the window will switch to next page
    When I click on the <combo> button
    Then the attendance box current select is <combo> box
    When I select start time at "2 AM" at <combo> box
      And I select end time at "5 PM" at <combo> box
    Then the start time at <combo> box text should be "2 AM" 
      And the end time at <combo> box text should be "5 PM"

    Examples:
      | combo         |
      | rent schedule |
      | rent reserve  |

  Scenario Outline: Check attendance box select rent reserve select single date
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
      And I click on the Next button
    Then the window will switch to next page
    When I click on the rent reserve button
    Then the attendance box current select is rent reserve box
    When I select date on "<date>"
    Then the select date at rent reserve box text should be "<date>"
      
    Examples:
      | date      |
      | Monday    |
      | Tuesday   |
      | Wednesday |
      | Thursday  |
      | Friday    |
      | Saturday  |
      | Sunday    |

  Scenario Outline: Check attendance box select rent reserve select multiple dates
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
      And I click on the Next button
    Then the window will switch to next page
    When I click on the rent reserve button
    Then the attendance box current select is rent reserve box
    When I select date on "<date1>"
      And I select date on "<date2>"
    Then the select date at rent reserve box text should be "<date1>"
      And the select date at rent reserve box text should be "<date2>"

    
    Examples:
      | date1     | date2     |
      | Monday    | Tuesday   |
      | Tuesday   | Thursday  |
      | Wednesday | Friday    |
      | Saturday  | Sunday    |

      