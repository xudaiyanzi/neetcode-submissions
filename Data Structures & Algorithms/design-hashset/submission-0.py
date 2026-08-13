class MyHashSet:

    def __init__(self):
        self.hash_k = 1000
        self.bucket = [[] for _ in range(1000)]

    def hash(self, key):
        return key % 1000

    def add(self, key: int) -> None:
        b = self.bucket[self.hash(key)]
        if key not in b:
            b.append(key)


    def remove(self, key: int) -> None:
        b = self.bucket[self.hash(key)]
        if key in b:
            b.remove(key)
              
    def contains(self, key: int) -> bool:
        if key in self.bucket[self.hash(key)]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)