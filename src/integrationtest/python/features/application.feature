# Created by sgomena at 9/26/18

Feature: High level application testing

    # TODO - setup user existing

  Scenario: Verify the application opens to dashboard
    Given the user is logged out of the application
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I click the login button
      And I open the application window
    Then the current tab should be the dashboard tab

  Scenario Outline: Verify the application stands up
    Given the user is logged out of the application
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I click on the <tab> tab
    Then the current tab should be the <tab> tab

    Examples:
      | tab       |
      | dashboard |
      | resources |
      | jobs      |
      | settings  |

  Scenario: Verify can logout and login again
    Given the user is logged out of the application
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I open the application window
      And I logout of the application
    Then the application window should be hidden
    When I wait 2 seconds
      # TODO: Have to 'manually' define the `login_window` object here; it should be done automatically
      And I open the login window
    Then the login window should be visible
