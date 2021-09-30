# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, of course).
def str_split(to_split, sep=" ", maxsplit=0):
    maxsplit = maxsplit or to_split.count(sep)  # if maxsplit given: maxsplit = given,else maxplit = all possible ways
    result = []
    for char in to_split:  # checking every char, may be it's not the best way but it's 2 AM and nobody will read
        # this long comment
        if char == sep and maxsplit != 0:
            index = to_split.index(char)  # temp value
            result.append(to_split[:index])
            to_split = to_split[index + 1:]  # cutting our string
            maxsplit -= 1
    result.append(to_split)
    return result  # I think i was abble to write a better program(not checking every char)


some_string = "Apple,banana,mango and melon"
another_string = "Return a list of the words in the string using sep as the delimiter string"
last_string = "1 2 3 4 5 6 7 8 9 0"

print(str_split(some_string, ","))
# print(some_string.split(","))
print(str_split(another_string))
# print(another_string.split())
print(str_split(last_string, maxsplit=2))
# print(last_string.split(maxsplit=2))
