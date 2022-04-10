"""
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/solution/
1101. The Earliest Moment When Everyone Become Friends
"""
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if x == self.root[x]: return x
        return self.find(self.root[x])

    def union(self, x,y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.root[y] = x
            return True
        return False

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
         1 2 3 4 5 6
        [0,0,3,3,3,0]
        """
        logs.sort(key=lambda x: x[0])
        group_counter = n
        uf = UnionFind(n)
        for timeStamp, friend_x, friend_y in logs:
            if uf.union(friend_x, friend_y):
                group_counter -= 1
            if group_counter == 1:
                return timeStamp
        return -1