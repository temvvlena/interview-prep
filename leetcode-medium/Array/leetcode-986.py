"""
https://leetcode.com/problems/interval-list-intersections/solution/
986. Interval List Intersections
"""


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not secondList or not firstList: return []
        first, second = 0, 0
        res = []
        while first < len(firstList) and second < len(secondList):
            lower, higher = max(firstList[first][0], secondList[second][0]), min(firstList[first][1],
                                                                                 secondList[second][1])
            if higher >= lower: res.append([lower, higher])
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        return res
