from functools import reduce


class HashTable:
    def __init__(self):
        """
        ini
        """
        self.buckets = [None, None, None, None, None, None, None, ]

    def sum_hash(str):
        return reduce(lambda a, b: a + ord(b), list(str), 1)

    def mult_hash(str):
        return reduce(lambda a, b: a * ord(b), list(str), 1)

    def put(self, key, value):
        hash = self.sum_hash(key)
        index = hash % len(self.buckets)
        self.buckets[index] = value

    def get(self, key):
        hash = self.sum_hash(key)
        index = hash % len(self.buckets)
        return self.buckets[index]

    def update(self, key, value):
        hash = self.sum_hash(key)
        index = hash % len(self.buckets)
        self.buckets[index] == value

    def keys(self):
        keys = []
        for k in self.buckets:
            keys.append(k)

