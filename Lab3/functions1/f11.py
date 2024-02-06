def is_palindrome(word):
    word = "".join(word.split())
    return word == word[::-1]

