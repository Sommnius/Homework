# Implement a decorator `remember_result` which remembers last result 
# of function it decorates and prints it before next call.


def remember_result(func):
    last_result = None

    def wrapper(*args, **kwargs):
        nonlocal last_result
        print(f"Last result:'{last_result}'")
        last_result = func(*args, **kwargs)
        # return last_result

    return wrapper


@remember_result
def sum_list(*args):
    for elem in args:
        if isinstance(elem, int):
            result = 0
        else:
            result = ""
            break
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)
