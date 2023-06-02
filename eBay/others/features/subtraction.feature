# Created by Jatin-PC at 5/29/2023
Feature: Perform an Subtraction Feature
  # Enter feature description here

  Scenario Outline: Subtraction of Two number
    Given take the "<first_number>" and "<second_number>"
    When subtract "<first_number>" and "<second_number>"
    Then Print the total result
    Examples:
      | first_number | second_number |
      |4             |2              |
      |2             |0              |
      |-2            |0              |
      |-2            |-2             |