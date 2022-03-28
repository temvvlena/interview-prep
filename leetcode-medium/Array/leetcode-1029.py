"""
https://leetcode.com/problems/two-city-scheduling/
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = []
        i = 0
        while i < len(costs):
            res.append([costs[i][1] - costs[i][0], i])
            i += 1
        res.sort()
        # [[-350, 2], [-10,3], [10,0], [170,1]]
        half = int(len(costs)/2 )
        output = 0

        cityB = res[0:half]
        cityA = res[half::]

        index = 0
        while index < len(cityA):
            getIndexB = cityB[index][1]
            getIndexA = cityA[index][1]
            output += costs[getIndexA][0]
            output += costs[getIndexB][1]
            index += 1
        return output