a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # global a
        a = "I am local variable!"
        print(a)

    # return inner_function()

# Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# add return inner_function
enclosing_funcion()

# Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# Delete "a=I am global variable" and add "global a"

# Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
# Delete "global a"