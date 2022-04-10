"""
https://leetcode.com/problems/all-paths-from-source-to-target/
Leetcode 797
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        def dfs(node, path, output):
            if node == end: output.append(path)
            for i in graph[node]: dfs(i, path+[i], output)
        output = []
        dfs(0, [0], output)
        return output