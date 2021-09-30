# Write a Python program to convert a given tuple of positive integers into an integer.



data = input("Give me numbers(comma separated):\n")
some_tuple = tuple(data.split(','))  # creating tuple from a string
result = ''.join(some_tuple)
print(result)
