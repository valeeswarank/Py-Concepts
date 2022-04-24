# Hash map/Hash table refers pythons dictionary. In this class we can try to define our own hash table class.
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        print(h)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    t = HashTable()
    t["valee"] = 100
    t["rishi"] = 200
    t["vaishu"] = 190
    t["bhuvana"] = 300
    t["test"] = 600

    print (t.arr)
    del t["test"]
    print(t.arr)