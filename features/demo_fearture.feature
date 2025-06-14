Feature:

  Scenario:
    Given User open agri chain home page
    Then User verifies home page

  Scenario:
    Given User open hrm login page
    When User open orange hrm home page
    And User enters username "Admin" and password "admin123"
    And User clicks login button
    Then User successfully login to dashboard page