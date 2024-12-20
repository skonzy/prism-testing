# string_utils.py
def capitalize_words(sentence):
    """
    Capitalizes the first letter of each word in a sentence.
    """
    return ' '.join(word.capitalize() for word in sentence.split())

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def reverse_string(s):
    """
    Reverses a string.
    """
    return s[::-1]

def remove_duplicates(s):
    """
    Removes duplicate characters from a string.
    """
    return ''.join(sorted(set(s), key=s.index))

def count_vowels(s):
    """
    Counts the number of vowels in a string.
    """
    return sum(1 for c in s if c.lower() in 'aeiou')

def count_consonants(s):
    """
    Counts the number of consonants in a string.
    """
    return sum(1 for c in s if c.isalpha() and c.lower() not in 'aeiou')

def count_words(s):
    """
    Counts the number of words in a string.
    """
    return len(s.split())

def count_characters(s):
    """
    Counts the number of characters in a string.
    """
    return len(s)

def count_lines(s):
    """
    Counts the number of lines in a string.
    """
    return s.count('\n') + 1

def count_occurrences(s, sub):
    """
    Counts the number of occurrences of a substring in a string.
    """
    return s.count(sub)

def remove_whitespace(s):
    """
    Removes all whitespace characters from a string.
    """
    return ''.join(s.split())

def remove_punctuation(s):
    """
    Removes all punctuation characters from a string.
    """
    return ''.join(c for c in s if c.isalnum() or c.isspace())

def remove_digits(s):
    """
    Removes all digit characters from a string.
    """
    return ''.join(c for c in s if not c.isdigit())

def remove_special_characters(s):
    """
    Removes all special characters from a string.
    """
    return ''.join(c for c in s if c.isalnum())

def remove_newline(s):
    """
    Removes all newline characters from a string.
    """
    return s.replace('\n', '')

def remove_tabs(s):
    """
    Removes all tab characters from a string.
    """
    return s.replace('\t', '')

def remove_spaces(s):
    """
    Removes all space characters from a string.
    """
    return s.replace(' ', '')

def remove_empty_lines(s):
    """
    Removes all empty lines from a string.
    """
    return '\n'.join(line for line in s.split('\n') if line.strip())

def remove_empty_lines_v2(s):
    """
    Removes all empty lines from a string.
    """
    return '\n'.join(line for line in s.split('\n') if line)