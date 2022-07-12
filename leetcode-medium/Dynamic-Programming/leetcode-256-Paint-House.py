"""
https://leetcode.com/problems/paint-house/
256-Paint House
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[8, 4, 10], [6, 3, 19], [4, 8, 12]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = []
Output: 0
Example 3:

Input: costs = [[7,6,2]]
Output: 2
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Dynamic programming and O N time complexity and O 1 space complexity
        """
        [[17,2,17],[8, 4, 10], [6, 3, 19], [4, 8, 12]]
        [4, 8, 12], [6, 3, 19], [8, 4, 10], [17, 2, 17]
        """
        """
        if costs == []: return 0
        for i in reversed(range(len(costs)-1)):
            costs[i][0] += min(costs[i+1][1], costs[i+1][2]) 
            costs[i][1] += min(costs[i+1][0], costs[i+1][2]) 
            costs[i][2] += min(costs[i+1][0], costs[i+1][1])
        return min(costs[0])
        """
        # Time and Space both O(N) 
        if costs == []: return 0
        def helper(n, color):
            if (n, color) in self.memo: return self.memo[(n, color)]
            total_cost = costs[n][color]  
            if n == len(costs)-1: pass
            elif color == 0: # Red
                total_cost += min(helper(n+1, 1), helper(n+1, 2))
            elif color == 1: # Green
                total_cost += min(helper(n+1, 0), helper(n+1, 2))
            elif color == 2: # Red
                total_cost += min(helper(n+1, 0), helper(n+1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost
        self.memo = {}
        return min(helper(0, 0), helper(0, 1), helper(0, 2))
        