# Created by Jatin-PC at 5/31/2023

@products.smoke @smoke
Feature: Product API Smoke
  # Enter feature description here

  @TCID-24
  Scenario: Verify 'get all products' returns the expected number of products
    Given I get number of available product from db
    When I get number of available product from api
    Then total number of products in api and db should be same


  @TCID-25
  Scenario: Verify 'products/id' returns the product with the given id
    Given Get "1" random product from Database
    When Verify the product api return the correct product id.
    Then verify API name and DB post title are same