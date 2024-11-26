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

def calculate_correlation(x, y):
    """
    Calculates the correlation between two lists of numbers.
    """
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    n = len(x)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n))) * math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
    return numerator / denominator

def calculate_covariance(x, y):
    """
    Calculates the covariance between two lists of numbers.
    """
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    n = len(x)
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n

def calculate_z_scores(numbers):
    """
    Calculates the z-scores of a list of numbers.
    """
    mean = calculate_mean(numbers)
    std_dev = calculate_standard_deviation(numbers)
    return [(x - mean) / std_dev for x in numbers]

def calculate_outliers(numbers):
    """
    Identifies outliers in a list of numbers.
    """
    z_scores = calculate_z_scores(numbers)
    return [numbers[i] for i, z in enumerate(z_scores) if abs(z) > 3]