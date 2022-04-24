
def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        sorted = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                sorted = True

        if not sorted:
            break


if __name__ == "__main__":
    #elements = [9, 29, 7, 2, 15, 28, 39]
    #elements = [5, 9, 2, 1, 67, 34, 88, 34]
    elements = [1, 2, 3, 4]
    elements = ["valee", "bhuvana", "rishi", "vaishu"]

    bubble_sort(elements)
    print(elements)