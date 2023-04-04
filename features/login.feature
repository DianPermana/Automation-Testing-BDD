# Created by aljazari at 4/4/2023
Feature: OrangeHRM Login

Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch to Chrome Browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click in login button
    Then User must successfully login to the Dashboard page
    Examples:
    | username | password |
    | admin    | admin123 |
    | admin123 | admin    |
    | adminxyz | admin123 |
    | admin    | adminxyz |