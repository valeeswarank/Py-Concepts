list1 = [12, 45, 67, 67, 70, 78, 78, 89, 89, 90]

print("before sort", list1)
list1.sort() # i think this is unnecessary
print("after sort ", list1)
print("set", set(list1))
#print("finally", list(list(set(list1)).sort())[-5:])
print(sorted(list(set(list1)))[-5:])

