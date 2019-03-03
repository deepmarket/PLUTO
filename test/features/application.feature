# Created by sgomena at 9/26/18

Feature: High level application testing
  # Enter feature description here

  Scenario: Verify the application opens to dashboard
    When I spin up the application
      And I open the login window
      And I login in to the application
#      And I enter "samgomena@gmail.com" in the username input box
#      And I enter "password" in the password input box
      And I click the login button
      And I open the application window
    Then the current tab should be the dashboard tab

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

  Scenario: Verify can logout and login again
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I wait 1 second
      And I logout of the application
    Then the login window should be displayed
