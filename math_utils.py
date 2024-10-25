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
