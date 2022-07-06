"""
https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/
380. Insert Delete GetRandom O(1)
"""


class RandomizedSet:
    def __init__(self):
        self.res = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.res: return False
        self.res[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.res:
            return False
        last_element, idx = self.array[-1], self.res[val]
        self.array[idx], self.res[last_element] = last_element, idx
        self.array.pop()
        del self.res[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
