# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.

def get_digits(num: int):
    return tuple(int(c) for c in str(num))  # easy


print(get_digits(87178291199))