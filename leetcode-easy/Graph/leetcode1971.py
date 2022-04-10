"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if x == self.root[x]:
            return x
        return self.find(self.root[x])

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.root[y] = x

    def returnsRoot(self):
        return self.root

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.find(source)== uf.find(destination)
