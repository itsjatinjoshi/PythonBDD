# Created by Jatin-PC at 5/25/2023
Feature: User Login First Time
  # Enter feature description here

  Scenario: Login a new User
    # Enter steps here
    Given Enter User's Credentials
    When Click on Login button
    Then Verify it will return 200 response message
