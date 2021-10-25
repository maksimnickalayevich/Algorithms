from typing import List, Tuple


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr: List[List[Tuple]] = [[] for _ in range(self.MAX)]

    def checksum(self, key):
        chsum = 0
        for c in key:
            chsum += ord(c)
        return chsum % self.MAX

    def __setitem__(self, key, value):
        exist = False
        placeIndex = self.checksum(key)

        for i, elem in enumerate(self.arr[placeIndex]):
            if elem[0] == key:
                self.arr[placeIndex][i] = (key, value)
                exist = True
                break
        if not exist:
            self.arr[placeIndex].append((key, value))

    def __getitem__(self, item):
        placeIndex = self.checksum(item)
        for t in self.arr[placeIndex]:
            if t[0] == item:
                return t[1]
        return None

    def __repr__(self):
        repr = []
        for i, v in enumerate(self.arr):
            if not v:
                continue
            repr.append(v)

        return f"<{', '.join([str(v) for v in repr])}>"

    def __delitem__(self, key):
        placeIndex = self.checksum(key)
        for i, t in enumerate(self.arr[placeIndex]):
            if t[0] == key:
                del self.arr[placeIndex][i]
                break
            raise AttributeError(key)

    def __len__(self):
        length = [v for v in self.arr if v]
        return len(length)
