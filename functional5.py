# Closure
# When we define a function returns a other function, that function still has access the internal scope of the variable

def create_printer():
    my_favorite_number = 3

    def printer():
        print(f"My favourite number is {my_favorite_number}")

    return printer

my_printer = create_printer()
# The following function still has the access to the local variable which is inside the function
my_printer()

def create_counter():
    count = 0

    def get_count():
        return count

    def increament():
        nonlocal count # defining non local variable, it will be as outside function
        count += 1

    return (get_count, increament)

get_count, increment = create_counter()
print(get_count())
increment()
increment()
print(get_count())
increment()
increment()
print(get_count())