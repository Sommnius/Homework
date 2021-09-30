# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.
def marks_replace(some_string):
    if "\'" in some_string:
        return some_string.replace("\'", "\"")
    return some_string.replace( "\"", "\'")



some_string = "Don't, it's, o'clock"
another_string = "Don\"t, it\"s, o\"clock"
print(marks_replace(some_string))
print(marks_replace(another_string))
