# Implement a function which search for most common words in the file.

def most_common_words(filepath, number_of_words=3):
    with open(filepath, "r") as file:
        data = file.read()
    data = data.replace("\n", "").replace(",", "").replace(".", "").casefold()
    # removing all dots,comas and
    data_list = data.split()
    data_set = set(data_list)
    result = {}
    for word in data_set:
        result.update({word: data_list.count(word)})
    return sorted(result, key=result.__getitem__, reverse=True)[:number_of_words]
    # if you use print provided below,you will get different result every time
    # you run this program.But the program is correct!!
    #


print(most_common_words('data/lorem_ipsum.txt', 10))
