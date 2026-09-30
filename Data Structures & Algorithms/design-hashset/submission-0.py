class MyHashSet:

    def __init__(self):
        self.hashSet = [0]
        

    def add(self, key: int) -> None:
        while key >= len(self.hashSet):
            self.hashSet += ([0] * len(self.hashSet))
        self.hashSet[key] = 1

        

    def remove(self, key: int) -> None:
        if key >= len(self.hashSet):
            return
        self.hashSet[key] = 0
        

    def contains(self, key: int) -> bool:
        if key >= len(self.hashSet):
            return False
        return self.hashSet[key] == 1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)