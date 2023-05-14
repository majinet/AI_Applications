Feature: Calculator

As a user of the calculator
I want to be able to perform basic arithmetic operations
So that I can calculate numbers

Scenario: Add two numbers
Given I have entered first number "5" into the calculator
And I have entered second number "6" into the calculator
When I press the "add" button
Then the result should be "11" on the screen

Scenario: Subtract two numbers
Given I have entered first number "9" into the calculator
And I have entered second number "4" into the calculator
When I press the "subtract" button
Then the result should be "5" on the screen

Scenario: Multiply two numbers
Given I have entered first number "3" into the calculator
And I have entered second number "8" into the calculator
When I press the "multiply" button
Then the result should be "24" on the screen

Scenario: Divide two numbers
Given I have entered first number "15" into the calculator
And I have entered second number "3" into the calculator
When I press the "divide" button
Then the result should be "5" on the screen