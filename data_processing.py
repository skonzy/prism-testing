# data_processing.py
import math

def calculate_mean(numbers):
    """
    Calculates the mean of a list of numbers!
    """
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """
    Calculates the median of a list of numbers.
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid - 1] + numbers[mid]) / 2 if n % 2 == 0 else numbers[mid]

def calculate_standard_deviation(numbers):
    """
    Calculates the standard deviation of a list of numbers.
    """
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
