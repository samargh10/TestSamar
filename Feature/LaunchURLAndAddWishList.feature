Feature: Launch URL and Add products in wishlist
  Scenario: Launch URL, Add products to wishlist and compare prices
    Given I launch the URL
    Then I should see the home page
    When I click on Shop menu
    Then I should be able to add four different products to wish list
    When I click on Wish list
    Then I should see the Wish list page
    And all the four products should be displayed
    Then I compare the prices of products and select lowest price product
    And add the selected product to cart
    When I click on Cart
    Then I should be able to see the least priced product displayed in cart



