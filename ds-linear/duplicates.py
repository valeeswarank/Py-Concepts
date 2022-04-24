nums = [2, 3, 4, 2, 3, 4, 5, 6]

dup = []
for n in nums:
    if not n in dup:
        dup.append(n)
    else:
        print("duplicate number", n)

# find a number in the list
find_num = 88

if find_num in nums:
    print("number 5 found")


