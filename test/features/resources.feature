# Created by sgomena at 6/22/19
Feature: Verify Functionality Around Resources
  # Enter feature description here

  Scenario: Resource List View
    When I spin up the application
      And I open the login window
      And I login in to the application
      And I click the log in button
      And I open the application window
      And I click on the resources tab
    Then the current resources tab should be the workspace view

    When I click on the resources list view tab
    Then the current resources tab should be the list view