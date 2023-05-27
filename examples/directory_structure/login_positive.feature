# Created by Jatin-PC at 5/25/2023
Feature: Get the correct user credentials
  # Enter feature description here

  Scenario: User loged in with correct username and passord

    Given Enter the correct credentials
    Then Click on the login button
    When Print 'Welcome on home Screen with Username'