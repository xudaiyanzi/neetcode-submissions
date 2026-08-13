class MyHashMap:

    def __init__(self):
        hash_key = 1000
        self.buckets = [[] for _ in range(hash_key)]
    
    def hash(self, key):
        return key % 1000

    def put(self, key: int, value: int) -> None:
        b = self.buckets[self.hash(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return
        b.append((key, value))
        

    def get(self, key: int) -> int:
        b = self.buckets[self.hash(key)]
        for (k, v) in b:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        b = self.buckets[self.hash(key)]
        for (k, v) in b:
            if k == key:
                b.remove((k, v))
                return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)