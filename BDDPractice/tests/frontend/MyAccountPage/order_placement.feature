# Created by Jatin-PC at 6/5/2023

@order_placement_smoke
Feature: Order Placement
  # Enter feature description here

  Scenario: New user place order with 1 item without creating an account
    Given I go to "home" page
    And Verify the title should be "mystore"
    When I added a random item into the cart
    And click on navigation cart button on the home page
    And Verify the title of "Cart" page
    And click on "proceed to checkout" button
    And Verify "Checkout" page is loaded
    And Fill all the necessary details in billing details form
    And verify "Flat rate" is selected
    And "Cash on delivery" method is selected
    And click on "Place order" button
    Then verify "Order received" page loaded with correct data
    And verify order is created in database
