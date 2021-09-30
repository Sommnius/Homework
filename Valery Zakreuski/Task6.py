# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.

def get_longest_word(s: str):
    s = s.replace("\t", " ").replace("\n", " ")
    longest = ""
    for word in s.split(" "):
        if len(word) > len(longest):
            longest = word
    return longest


print(get_longest_word('Python is simple and effective!'))
print(get_longest_word('Any pythonista like namespaces a lot.'))
