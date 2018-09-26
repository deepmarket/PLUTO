
Feature: High level API testing

  Scenario: verify the API is running properly
    Given the api is running
#     Then a "GET" request to "/api/v1/json" should reply with a status of 200
      Then a "GET" request to "/api/v1/" should reply with a status of None
