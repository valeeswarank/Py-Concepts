# Returning Functions

def create_printer():
    def printer():
        print("Hello functional!")
    return printer


my_printer = create_printer()
my_printer()

# Instead of using the following functions
# def double(x):
#     return x * 2
#
#
# def triple(x):
#     return x * 3
#
#
# def quadruple(x):
#     return x * 4


def creat_multiplier(a):
    def multiplier(x):
        return x * a
    return multiplier

double = creat_multiplier(2)
triple = creat_multiplier(3)
quardple =  creat_multiplier(4)

print(double(5))
print(triple(6))
print(quardple(7))