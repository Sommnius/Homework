# Write a Python program to print all unique values of all dictionaries in a list.


list_of_dicts = [{"V": "S001"},
                 {"V": "S002"},
                 {"VI": "S001"},
                 {"VI": "S005"},
                 {"VII": "S005"},
                 {"V": "S009"},
                 {"VIII": "S007"},
                 ]
temp = set(value for dict_i in list_of_dicts for value in dict_i.values())
print(temp)

# was trying to make an input,but failed

