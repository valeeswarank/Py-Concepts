def count_down(x):
    # Make sure to define the condition for the endpoint otherwise this will be infinitive
    if x < 0:
        print("Done!")
        return
    print(x)
    count_down(x - 1)


count_down(10)


def count_up(x, maximum):
    # Make sure to define the condition for the endpoint otherwise this will be infinitive
    if x > maximum:
        print("Done!")
        return
    print(x)
    count_up(x + 1, maximum)


count_up(0, 10)