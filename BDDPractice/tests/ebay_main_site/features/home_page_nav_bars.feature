# Created by Jatin-PC at 5/26/2023
Feature: Navigation bars in the home page
  # Enter feature description here

  Scenario: Verify navigation bar on home page are visible
    Given Go to the site "website"
    Then the "Home" should be visible
    And the "Saved" should be visible
    And the "Fashion" should be visible
    And the "Sneakers" should be visible
    And the "Motors" should be visible
    And the "Electronics" should be visible