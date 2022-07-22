"""
https://leetcode.com/problems/island-perimeter/
463. Island Perimeter
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if row == 0:
                        up = 0
                    else:
                        up = grid[row - 1][col]
                    if col == 0:
                        left = 0
                    else:
                        left = grid[row][col - 1]
                    if row == len(grid) - 1:
                        right = 0
                    else:
                        right = grid[row + 1][col]
                    if col == len(grid[0]) - 1:
                        down = 0
                    else:
                        down = grid[row][col + 1]
                    perimeter += (4 - up - down - left - right)
        return perimeter
