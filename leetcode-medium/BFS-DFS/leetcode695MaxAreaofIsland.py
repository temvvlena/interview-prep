"""
Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""


# Time Number of Col * Number of Row
# Space N
class Solution:
    def __init__(self):
        self.count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(matrix, row, col):
            if 0<=row<=len(matrix)-1 and 0<=col<=len(matrix[0])-1 and matrix[row][col] == 1:
                matrix[row][col] = 8
                self.count += 1
                dfs(matrix, row+1, col)
                dfs(matrix, row-1, col)
                dfs(matrix, row, col+1)
                dfs(matrix, row, col-1)
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid, row, col)
                    res = max(self.count, res)
                    self.count = 0
        return res