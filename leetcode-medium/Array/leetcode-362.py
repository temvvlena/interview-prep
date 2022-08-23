"""
https://leetcode.com/problems/design-hit-counter/
Design Hit Counter
"""
from collections import deque


class HitCounter(object):
    def __init__(self):
        self.num_of_hits = 0
        self.time_hits = deque()

    def hit(self, timestamp):
        if not self.time_hits or self.time_hits[-1][0] != timestamp:
            self.time_hits.append([timestamp, 1])
        else:
            self.time_hits[-1][1] += 1
        self.num_of_hits += 1

    def getHits(self, timestamp):
        while self.time_hits and self.time_hits[0][0] <= timestamp - 300:
            self.num_of_hits -= self.time_hits.popleft()[1]
        return self.num_of_hits


"""
SOLUTION 1
from collections import deque
class HitCounter:

    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)

"""

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
