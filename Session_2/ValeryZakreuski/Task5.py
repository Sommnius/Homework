# Write a Python program to sort a dictionary by key.


dict_to_sort = {'apples': 2,
                'melons': 41,
                'bananas': 401,
                'pineapples': 0,
                'others': 5,
                }
sorted_dict = {fruit: dict_to_sort[fruit] for fruit in sorted(dict_to_sort)}
print(sorted_dict)
