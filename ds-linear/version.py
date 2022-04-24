import struct

# By default you can check the python version by typing the following command in consol
# python -b # this will give you the python application details in consol itself.
# For example
# Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Also you can check it in programatically by using struct pack

print(struct.calcsize("P")*8)

# Understand the 32bit and 64 bit
# In consol window type py -0p, it will print the following result
# Installed Pythons found by py Launcher for Windows
#  -3.7-32        C:\Python374\python.exe *
#  -2.7-64        C:\Python27\python.exe

# Here is the result for the output
# C:\Users\Valee>py -3.7-32
# Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> exit()
#
# C:\Users\Valee>py -2.7-64
# Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> ^Z