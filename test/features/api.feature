
Feature: High level API testing

  Scenario: Verify the api returns proper data
    Given the api is up
#     Then a "GET" request to "/api/v1/json" should reply with a status of 200
      When I send a "GET" request to "/api/vi/"
      Then the request should reply with a status of None


