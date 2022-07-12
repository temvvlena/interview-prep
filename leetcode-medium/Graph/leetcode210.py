"""
https://leetcode.com/problems/course-schedule-ii/
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
        result = []
        while zero_indegree_queue:
            vertex = zero_indegree_queue.popleft()
            result.append(vertex)
            for neighbor in adj_list[vertex]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)
        return result if len(result) == numCourses else []
