"""
https://leetcode.com/problems/unique-paths/
Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Time and Space O(N*M)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(1)
            matrix.append(temp)
        
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]