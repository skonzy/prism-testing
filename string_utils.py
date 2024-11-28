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