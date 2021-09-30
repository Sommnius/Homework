# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited.
import re


def is_palindrome(word, check=True):
    if check:  # need to remove all space's and other symbols like "! . , '"
        word = re.sub(r'[\W_]+', '', word.casefold())  # removing all useless chars and making string lower case
    if len(word) < 2:  # palindrome
        return "This string is a palindrome!"
    if word[0] == word[-1]:  # using recursion
        return is_palindrome(word[1:-1], False)
    return "No,it's not:("  # else


print(is_palindrome("a ca bb aca", True))  # Yes
print(is_palindrome("Mr. Owl ate my metal worm"))  # Yes
print(is_palindrome("123 456 789"))  # No
