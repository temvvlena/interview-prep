"""
https://leetcode.com/problems/number-of-provinces/
547. Number of Provinces
"""
class UnionFind:

    def __init__(self, size):
        self.n = size
        self.root = [i for i in range(size)]
        self.counter = size

    def find(self, v):
        if v == self.root[v]: return v
        return self.find(self.root[v])

    def union(self, v1, v2):
        v1, v2 = self.find(v1), self.find(v2)
        if v1 != v2:
            self.root[v2] = v1
            self.counter -= 1

    def returnCounter(self):
        return self.counter

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0: return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.returnCounter()