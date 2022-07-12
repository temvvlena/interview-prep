"""
https://leetcode.com/problems/number-of-provinces/
Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth 
city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""


# Time O(N Squared) and Space O(N)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # col oo bas davhar call hiine
        def dfs(matrix, row):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    isConnected[row][col] = -1
                    dfs(matrix, col)
        count = 0
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    count += 1
                    dfs(isConnected, row)
        return count        