"""
https://leetcode.com/problems/max-area-of-island/
Max Area of Island
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (0 > r or r >= len(grid)) or (0 > c or c >= len(grid[r])):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        maxNum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxNum = max(maxNum, dfs(row, col))
        return maxNum
