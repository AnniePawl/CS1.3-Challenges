#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and backwards, ignoring punctuation, whitespace, and letter casing."""
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """is_palindrome_iterative return True if input text is a palindrome, and false if not"""
    # Edge cases? Check if input = None or is weird
    palindrome = None
    reverse_text = text.reverse()
    if text == reverse_text:
        palindrome = True
    else:
        palindome = False

    # Quick check? Does 1st letter = last letter
    # for i in range(len(text)):
    #     # check if work spelled same way backward forward
    #     if blank:
    #         palindrome = True
    #     else:
    #         palindrome = False

    return palindrome


def is_palindrome_recursive(text, left=None, right=None):
    """is_palindrome_recursive return True if input text is a palindrome, and false if not"""
    # check if n is one of the base cases
    palindrome = None

    return is_palindrome_recursive(text)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    print(is_palindrome_iterative(text))
    print(is_palindrome_recursive(text))
