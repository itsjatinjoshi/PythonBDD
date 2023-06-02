
@smoke @user_api_smoke
# Created by Jatin-PC at 6/1/2023
Feature: User API Smoke
  # Enter feature description here

  @TCID-29
  Scenario: Verify 'POST /customers' create user
    Given Generate random email and password
#    When I call 'create customer' api
#    Then customer should created