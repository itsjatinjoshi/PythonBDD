# Created by Jatin-PC at 5/26/2023
Feature: Verify the home page url of ebay is correct
  # Enter feature description here

  Scenario: Verify ebay home page is have correct title
    Given Go to the site "website"
    Then Verify the title should be "Electronics, Cars, Fashion, Collectibles & More | eBay"

  Scenario: Verify the ebay home page url
    Given Go to the site "website"
    Then Verify the url should be "https://www.ebay.ca/"