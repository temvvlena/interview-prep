"""
https://leetcode.com/problems/all-paths-from-source-to-target/
Leetcode 797
"""
# BFS
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        [4,3,1],[3,2,4],[3],[4],[]
         0.      1       2.  3. 4

        """
        if not graph: return []
        q = deque()
        q.append([0])
        paths = []
        while q:
            current_path = q.popleft()
            node = current_path[-1]
            for neighbor in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(neighbor)
                if neighbor == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    q.append(temp_path)
        return paths

#DFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        def dfs(node, path, output):
            if node == end: output.append(path)
            for i in graph[node]: dfs(i, path+[i], output)
        output = []
        dfs(0, [0], output)
        return output

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        [4,3,1],[3,2,4],[3],[4],[]
         0.      1       2.  3. 4

        """
        def dfs(node):
            path.append(node)
            if node == len(graph)-1:
                paths.append(path.copy())
                return
            neighbors = graph[node]
            for neighbor in neighbors:
                dfs(neighbor)
                path.pop()

        if not graph or len(graph) == 1: return 0
        paths, path = [], []
        dfs(0)
        return paths
