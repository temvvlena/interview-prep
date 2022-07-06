"""
https://leetcode.com/problems/course-schedule-ii/
Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
"""
from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = defaultdict(list)
        for dest, src in prerequisites: adj_list[src].append(dest)
        color = {}
        for i in range(numCourses): color[i] = Solution.WHITE
        
        res = []
        colorChanged = False
        def helper(vertex):
            # Change the color to Gray
            nonlocal colorChanged
            if colorChanged is True: return
            color[vertex] = Solution.GRAY
            for neighbor in adj_list[vertex]:
                if color[neighbor] == Solution.WHITE:
                    helper(neighbor)
                elif color[neighbor] == Solution.GRAY:
                    colorChanged = True
            color[vertex] = Solution.BLACK
            res.append(vertex)
        
        for vertex in color.keys():
            if color[vertex] == Solution.WHITE:
                helper(vertex)
                
        if colorChanged: return []
        else: return res[::-1]
        
        