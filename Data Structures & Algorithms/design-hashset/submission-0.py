class MyHashSet:

    def __init__(self):
        self.hset = set()

    def add(self, key: int) -> None:
        self.hset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hset:
            self.hset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)