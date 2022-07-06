"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/solution/

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

class Solution:
    # Time and  Space O(MxN)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.helperFunction(grid, i, j)
        return count
    def helperFunction(self, grid, i, j):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "2"
            self.helperFunction(grid, i, j-1)
            self.helperFunction(grid, i, j+1)
            self.helperFunction(grid, i+1, j)
            self.helperFunction(grid, i-1, j)
            
        