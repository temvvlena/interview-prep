"""
https://leetcode.com/problems/flatten-2d-vector/
251. Flatten 2D Vector
"""


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

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
