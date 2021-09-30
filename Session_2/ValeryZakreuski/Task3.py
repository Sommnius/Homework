# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form.



some_sequence = input('Input sequence of words(comma separated):\n')
final_list = sorted(set(some_sequence.split(',')))
print(final_list)