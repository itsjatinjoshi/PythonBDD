# Created by Jatin-PC at 5/26/2023
Feature: Navigation bars in the home page
  # Enter feature description here

  Scenario: Verify navigation bar on home page are visible
    Given I go to the site "https://www.ebay.ca/"
    Then the "main navigation" bar should be visible
    And the "top navigation" bar should be visible
    And the "options" bat sould be visible