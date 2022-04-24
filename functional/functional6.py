# Higher order functions

# Writing in normal way
# def divide(x, y):
#     if y == 0:
#         print("Warning: the second argument value is 0")
#         return
#     return x / y


#print(divide(4, 1))


def devide(x, y):
    return x / y


# Wrapper function
def second_argument_isnt_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print("Warning: second argument is zero")
            return
        return func(*args)

    return safe_version

divid_safe = second_argument_isnt_zero(devide)
divid_safe(19, 0)
print(divid_safe(10, 2))