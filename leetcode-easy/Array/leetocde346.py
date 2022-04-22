"""
https://leetcode.com/problems/moving-average-from-data-stream/
346. Moving Average from Data Stream
"""

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.window_size = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.window_size += 1
        self.count += val

        if self.window_size > self.size:
            popLeft = self.q.popleft()
            self.count -= popLeft
            self.window_size -= 1
            return self.count / self.size

        return self.count / self.window_size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
