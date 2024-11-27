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