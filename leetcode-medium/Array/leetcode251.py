"""
https://leetcode.com/problems/flatten-2d-vector/
251. Flatten 2D Vector
"""
from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        def flatten(anArray):
            res = []
            for aList in anArray:
                res.extend(aList)
            return res

        self.vec = flatten(vec)
        self.position = -1

    def next(self) -> int:
        self.position += 1
        return self.vec[self.position]

    def hasNext(self) -> bool:
        return self.position != len(self.vec) - 1


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vector = vec
        self.outer = 0
        self.inner = 0

    def advanceToNext(self):
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.inner = 0
            self.outer += 1

    def next(self) -> int:
        self.advanceToNext()
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        self.advanceToNext()
        return len(self.vector) > self.outer

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
