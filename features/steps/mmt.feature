Feature: Make_My_Trip
  Background: Common code
    Given launch chrome browser
    When open make_my_trip page
    Then click bus module

  Scenario Outline: choose places
    Then enter the arrival places "<arival>"
    And enter the destination places "<destination>"
    And enter the date
    And click on serach
       Examples:
         |arival       |destination  |
         | Pune        | banglo      |
    And dismiss
    Then click on select seat button
    And select the seat
    And click on book seat button
    Then travel details
    And contact details
    Then select options
    And proceed to payment
