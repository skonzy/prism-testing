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

def fibonacci(n):
    """
    Calculates the nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b