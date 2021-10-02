# Open file `data/unsorted_names.txt` in data folder. Sort the names and write
# them to a new file called `sorted_names.txt`. Each name should start with a new line

with open("data/unsorted_names.txt") as file_in:
    names_list = list(name for name in file_in.readlines())
    names_list.sort()

with open("data/sorted_names.txt", "w") as file_out:
    for name in names_list:
        file_out.write(name)
