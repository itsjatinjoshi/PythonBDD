# Created by Jatin-PC at 5/29/2023
Feature: Perform an Addition Feature
  # Enter feature description here

  Scenario Outline: Sum of Two number
    Given take the "<first_number>" and "<second_number>"
    When calculate the sum of "<first_number>" and "<second_number>"
    Then Print the total result
    Examples:
      | first_number | second_number |
      |4             |2              |
      |2             |0              |
      |-2            |0              |
      |-2            |-2             |

