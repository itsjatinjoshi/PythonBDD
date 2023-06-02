# Created by Jatin-PC at 5/29/2023
Feature: Add taxes according to State
  # Enter feature description here

  Scenario Outline: Charge the uses appropriate tax according to <state>
    # Enter steps here
    Given I login as a User
    When I added a "total_price" book to the cart
    And Select the "<state>"
    Then Tax will calculate according to "<state>"

    Examples:
      | state |
      | CA    |
      | NY    |
      | TX    |
      | DC    |

  Scenario Outline: <Quantity> and <Payment_Method>
    Given I have "<Quantity>" of items
    When  I checked out using "<Payment_Method>"
    Then I got "percentage" of discount.

    Examples:
      | Quantity | Payment_Method |
      | 1        | credit card    |
      | 3        | debit card     |
      | 4        | master card    |
      | 5        | visa card      |
      | 10       | gift card      |
