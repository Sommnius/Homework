# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.

def split_by_index(s: str, indexes: [int]):
    length = len(s)
    result = []
    if indexes and indexes[-1] + 1 > length:
        return split_by_index(s, indexes[:-1])
    indexes.insert(0, 0)
    indexes.insert(length, length)
    indexes = list(zip(indexes[:-1], indexes[1:]))
    for index in indexes:
        result.append(s[index[0]:index[1]])
    return result


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))
