"""
https://leetcode.com/problems/course-schedule/
"""
from collections import defaultdict, deque
class GNode(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(GNode)
        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1
        nodeCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodeCourses.append(index)
        removedEdges = 0
        while nodeCourses:
            course = nodeCourses.pop()
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                if graph[nextCourse].inDegrees == 0:
                    nodeCourses.append(nextCourse)
        return removedEdges == totalDeps
