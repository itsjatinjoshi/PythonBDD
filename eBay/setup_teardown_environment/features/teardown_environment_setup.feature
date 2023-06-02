# Created by Jatin-PC at 5/29/2023
  @smoke
Feature: Test the teardown steps
  # Enter feature description here

  Scenario: set-up teardown steps
    Given Add 2 numbers
    When pass first num
    And pass second num
    Then verify sum
    And Verify Multiplication
    And verify subtraction
