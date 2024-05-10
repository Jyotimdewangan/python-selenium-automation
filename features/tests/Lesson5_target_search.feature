# Created by jyoti at 5/9/2024
Feature: Target Search
  # Enter feature description here

   Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image


   Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
#    And Store product name
#    And Confirm Add to Cart button from side navigation
#    And Open cart page
#    Then Verify cart has 1 item(s)
#    And Verify cart has correct product