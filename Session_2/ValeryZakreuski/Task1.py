# Write a Python program to calculate the length of a string without using the
# `len` function.



some_string, string_length = input("Input your string:\n"), 0
for char in some_string: string_length += 1
print(f"Length of your string: {string_length}")
