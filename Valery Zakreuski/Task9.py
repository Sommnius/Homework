# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
import string


def test_1_1(*strings):
    result = []
    for char in set(strings[0]):
        for word in strings[1:]:
            if char not in word:
                char_appear = False
                break
            char_appear = True
        if char_appear: result.append(char)
    return set(result)


def test_1_2(*strings):
    return set(char for word in strings for char in word)  # creating set of chars of every word


def test_1_3(*strings):
    result = []
    for first_word in strings[:-1]:
        index = strings.index(first_word)
        for second_word in strings[index + 1:]:
            for char in first_word:
                if char in second_word:
                    result.append(char)
    return set(result)


def test_1_4(*strings):
    used_chars = test_1_2(*strings)
    alphabet = string.ascii_lowercase
    result = []
    for char in alphabet:
        if char not in used_chars:
            result.append(char)
    return result


test_strings = ["hello", "world", "python", ]
# print(test_1_1(*test_strings))
test_strings_1 = ["123456789", "12345", "234", ]
# print(test_1_1(*test_strings_1))
# print(test_1_2(*test_strings))
# print(test_1_3(*test_strings))
# print(test_1_4(*test_strings))
