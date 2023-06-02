# Created by Jatin-PC at 5/29/2023
Feature: Perform an division Feature
  # Enter feature description here

  Scenario Outline: Divide the Two number
    Given take the "<first_number>" and "<second_number>"
    When verify if greater number between "<first_number>" and "<second_number>"
    And divide greater with lower
    Then Print the total result
    And if both are same, return 0
    Examples:
      | first_number | second_number |
      |4             |2              |
      |2             |0              |
      |-2            |0              |
      |-2            |-2             |