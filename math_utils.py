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

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """
    Generates the Fibonacci sequence up to a certain number of terms.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a
