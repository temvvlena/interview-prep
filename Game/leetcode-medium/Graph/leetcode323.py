"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
323. Number of Connected Components in an Undirected Graph
"""
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.counter = n
    def find(self, x):
        if x == self.root[x]: return x
        return self.find(self.root[x])

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.root[y] = x
            self.counter -= 1
    def countSize(self):
        return self.counter


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i in edges:
            uf.union(i[0], i[1])
        return uf.countSize()