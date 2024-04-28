# Created by jyoti at 4/27/2024
Feature: Target sign in page
  # Enter feature description here

  Scenario: User can navigate to Sign In:
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened


