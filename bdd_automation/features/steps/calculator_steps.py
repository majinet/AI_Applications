from behave import given, when, then
from bdd_automation.py.calculator import Calculator

calculator = Calculator()

@given('I have entered first number "{num1}" into the calculator')
def step_impl(context, num1):
    context.num1 = int(num1)

@given('I have entered second number "{num2}" into the calculator')
def step_impl(context, num2):
    context.num2 = int(num2)

@when('I press the "add" button')
def step_impl(context):
    context.result = calculator.add(context.num1, context.num2)

@when('I press the "subtract" button')
def step_impl(context):
    context.result = calculator.subtract(context.num1, context.num2)

@when('I press the "multiply" button')
def step_impl(context):
    context.result = calculator.multiply(context.num1, context.num2)

@when('I press the "divide" button')
def step_impl(context):
    context.result = calculator.divide(context.num1, context.num2)

@then('the result should be "{expected_result}" on the screen')
def step_impl(context, expected_result):
    assert context.result == float(expected_result)