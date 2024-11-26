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
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Calculates the least common multiple of two numbers.
    """
    return a * b // gcd(a, b)

def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams.
    """
    return sorted(s1) == sorted(s2)

def is_armstrong(n):
    """
    Checks if a number is an Armstrong number.
    """
    s = str(n)
    return n == sum(int(c) ** len(s) for c in s)

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    """
    return s == s[::-1]

def is_perfect(n):
    """
    Checks if a number is a perfect number.
    """
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_power_of_two(n):
    """
    Checks if a number is a power of two.
    """
    return n > 0 and n & (n - 1) == 0
