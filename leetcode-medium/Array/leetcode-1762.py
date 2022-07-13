"""
https://leetcode.com/problems/buildings-with-an-ocean-view/
1762. Buildings With an Ocean View
"""


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        for index, value in enumerate(heights):
            while buildings and value >= heights[buildings[-1]]: buildings.pop()
            buildings.append(index)
        return buildings
