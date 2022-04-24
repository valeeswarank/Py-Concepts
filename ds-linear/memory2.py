# Compare size for 1M int elements stored in list, tuple, set, dict
# Tuple requires less space compare to list. Set and dictionary requires more space compare to list and tuple.
# Tuple requires average 8 bytes per element, list requires average 9 bytes per element, set requires average
# 33 bytes per element, dictionary requires average 41 bytes per pair. This comparison is for int data used in
# list, tuple, set, dict.
# Memory size may not be the only criteria to select data type. Rather, time required to perform operation
# on data type can be critical criteria.

import sys

a1 = list(range(0, 10**6))
a2 = tuple(range(0, 10**6))
a3 = set(range(0, 10**6))
a4 = dict(zip(range(0, 10**6),  range(0, -1 * 10**6, -1)))

print(len(a1))
print(len(a2))
print(len(a3))
print(len(a4))

print(sys.getsizeof(a1) / len(a1))
print(sys.getsizeof(a2) / len(a2))
print(sys.getsizeof(a3) / len(a3))
print(sys.getsizeof(a4) / len(a4))


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


print("Size of 1M integer in list  : ", convert_bytes(sys.getsizeof(a1)))
print("Size of 1M integer in tuple : ", convert_bytes(sys.getsizeof(a2)))
print("Size of 1M integer in set   : ", convert_bytes(sys.getsizeof(a3)))
print("Size of 1M integer in dict  : ", convert_bytes(sys.getsizeof(a4)))
