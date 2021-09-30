# Write a Python program to count the number of characters 
# (character frequency) in a string (ignore case of letters).



your_string = input("Give me some string\n").lower()
final_dict = {character: your_string.count(character) for character in your_string}
print(final_dict)
