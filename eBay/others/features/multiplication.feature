# Created by Jatin-PC at 5/29/2023
Feature: Perform an Multiplication Feature
  # Enter feature description here

  Scenario Outline: Multiplication of Two number
    Given take the "<first_number>" and "<second_number>"
    When multiply "<first_number>" and "<second_number>"
    Then Print the total result
    Examples:
      | first_number | second_number |
      |4             |2              |
      |2             |0              |
      |-2            |0              |
      |-2            |-2             |