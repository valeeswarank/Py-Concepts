import os.path
import sys

# Hash map/Hash table refers pythons dictionary. In this class we can try to define our own hash table class.
class HashTable:
    def __init__(self):
        self.MAX = 25
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))


    def __getitem__(self, item):
        h = self.get_hash(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if index == key:
                del self.arr[h][key]



if __name__ == '__main__':
    t = HashTable()
    #with open(sys.path.par()
    raw_dir = r'D:\Projects\Python\tutorials\data\raw'
    sfile = os.path.join(raw_dir, "nyc_weather.txt")
    lines = ""
    with open(sfile, mode="r", encoding="utf-8") as f:
        lines = f.readlines()[1:]


    for line in lines:
        str = line.strip().split(",")
        print(t.get_hash(str[0]), str[0], str[1])
        t[str[0]] = str[1]

    print(t["Jan 9"])
    print(t["Jan 4"])
