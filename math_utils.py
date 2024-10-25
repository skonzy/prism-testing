# math_utils.py
def add_numbers(a, b):
    """
    Adds two numbers together.
    """
    return a + b

def multiply_numbers(a, b):
    """
    Multiplies two numbers together.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divides two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """
    Calculates the factorial of a number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
