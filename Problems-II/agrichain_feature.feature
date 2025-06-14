Feature: Longest Substring Output
  Background:
    Given User open agri chain home page

  Scenario: TC01 : Enters valid input & get correct output
    When User enters "abcabcbb" into the input field
    And User clicks the submit button
    Then User should see the output "abc"

  Scenario: TC02 : Input with digits and check result
    When User enters "a1b2c3d4" into the input field
    And User clicks the submit button
    Then User should see the output "a1b2c3d4"