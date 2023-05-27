# Created by Jatin-PC at 5/25/2023
Feature: All negative login Steps
  # Enter feature description here

  Scenario: Fail login with wrong username
    # Enter steps here
    Given Enter the Wrong username.
    When  Click on the login button
    Then Send an error wih 'user not found'

  Scenario: Fail login with wrong password
    # Enter steps here
    Given Enter the Wrong password.
    When  Click on the login button
    Then Send an error wih 'wrong password'

  Scenario: Fail login with empty username
    # Enter steps here
    Given leave the username box empty.
    When  Click on the login button
    Then Send an error wih 'Please enter the username'

  Scenario: Fail login with empty password
    # Enter steps here
    Given leave the password box empty.
    When  Click on the login button
    Then Send an error wih 'Please enter the password'