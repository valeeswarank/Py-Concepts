import sys
from decimal import Decimal
# This module will help you to undestand, how python memory used.

def getsize(x, msg=''):
    print(msg.ljust(20), "==>", str(sys.getsizeof(x)).ljust(3), " bytes")


getsize(5, "Integer")
getsize(5.3, "Float")
getsize(Decimal(5.3), "Decimal")
getsize('', "Empty String")
getsize('1', "String")
getsize('1234', "String")
getsize(u'', "Empty unicode")
getsize(u'1', "Unicode string")
getsize(u'1234', "Unicode String")
getsize(list, "List")


# Understanding the size of objects
# getsize(int)
# getsize(float)
# getsize(list)
# getsize(tuple)
# getsize(dict)
# getsize(bool)

# Checking the instances of the above classes
# getsize(int())
# getsize(float())
# getsize(list())
# getsize(tuple())
# getsize(dict())
# getsize(bool())


