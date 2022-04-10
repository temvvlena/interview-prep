"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""

# BFS
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        q = deque([start])
        seen = set([start])
        while q:
            node = q.popleft()
            if node == end:
                return True
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
        return False

# DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for i, j in edges:
            adj_list[i].append(j) # [1,2][2,0][0,1]
            adj_list[j].append(i)
        stack = [start]
        seen = set()
        while stack:
            top = stack.pop()
            if top == end: return True
            if top in seen:
                continue
            seen.add(top)
            for i in adj_list[top]:
                stack.append(i)
        return False

"""
UnionFind Below
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
        for i, j in edges:
            uf.union(i, j)
        return uf.find(source)== uf.find(destination)
