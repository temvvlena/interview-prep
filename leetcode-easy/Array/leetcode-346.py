"""
https://leetcode.com/problems/moving-average-from-data-stream/
346. Moving Average from Data Stream
"""
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.myArray = deque()
        self.size = size
        self.counter = 0

    def calculateAverage(self, val):
        self.myArray.append(val)
        return float(sum(self.myArray) / len(self.myArray))

    def next(self, val: int) -> float:
        if self.counter < self.size:
            self.counter += 1
            return self.calculateAverage(val)
        else:
            self.myArray.popleft()
            return self.calculateAverage(val)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
