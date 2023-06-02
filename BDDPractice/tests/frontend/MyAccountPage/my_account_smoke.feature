# Created by Jatin-PC at 5/30/2023

  @my_account_smoke
  Feature: My Account Smoke Tests
    # Enter feature description here

    Scenario: Valid User able to login

      Given I go to "my account" page
      When I type "first.test.user@supersqa.com" to the username of login form
      And I type "testuserpassw" to the login form
      And I click on "login" button
      Then user should be logged in

    Scenario: User with wrong password should get error message
      Given I go to "my account" page
      When I type "first.test.user@supersqa.com" to the username of login form
      And I type "testuserpassw2" to the login form
      And I click on "login" button
      Then user should get an error message for related to entered email "first.test.user@supersqa.com"

    @TCID-12
    Scenario: User with wrong email should get error message
      Given I go to "my account" page
      When I type "first.test.user@supersqa.com1" to the username of login form
      And I type "testuserpassw" to the login form
      And I click on "login" button
      Then user should get an error message unknown email address