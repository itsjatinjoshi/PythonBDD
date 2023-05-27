# Created by Jatin-PC at 5/25/2023
Feature: Create a table with different parameters
  # Enter feature description here

  Scenario: Enter an int value and create table upto 10
    Given Enter a int "5"
    When Multiply "5" up to 10
    Then Verify "5" run 10 times