"""A simple calculator program using BDD Cucumber feature syntax"""

class Calculator:
    def add(self, num1: int, num2: int) -> int:
        """
        Add two numbers and return the result.
        :param num1: First operand for addition
        :param num2: Second operand for addition
        :return: Result of addition
        """
        return num1 + num2

    def subtract(self, num1: int, num2: int) -> int:
        """
        Subtract num2 from num1 and return the result.
        :param num1: First operand for subtraction
        :param num2: Second operand for subtraction
        :return: Result of subtraction
        """
        return num1 - num2

    def multiply(self, num1: int, num2: int) -> int:
        """
        Multiply two numbers and return the result.
        :param num1: First operand for multiplication
        :param num2: Second operand for multiplication
        :return: Result of multiplication
        """
        return num1 * num2

    def divide(self, num1: int, num2: int) -> float:
        """
        Divide num1 by num2 and return the result as float.
        :param num1: Numerator for division
        :param num2: Denominator for division
        :return: Result of division as float
        """
        return num1 / num2