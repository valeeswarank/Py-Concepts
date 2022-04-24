import pprint

def bubble_sort(elements, keyvalue):
    size = len(elements)

    for i in range(size - 1):
        sorted = False
        key = [key for key in elements[i] if key == keyvalue][0]
        val = elements[i][key]
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                sorted = True

        if not sorted:
            break





if __name__ == "__main__":
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixcel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "rishi", "transaction_amount": 800, "device": "samsung"},
    ]

    pprint.pprint(elements, indent=4)
    bubble_sort(elements, keyvalue="transaction_amount")
    print("\n\n")
    pprint.pprint(elements, indent=4)
