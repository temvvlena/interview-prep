"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
Shortest Path in Binary Matrix
"""
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1,0), (1,1)]

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        def get_neighbours(row, col):
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff
                if not (0 <= new_row<=max_row and 0<=new_col<=max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        q = deque()
        q.append((0,0))
        grid[0][0] = 1

        while q:
            row, col = q.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                q.append((neighbour_row, neighbour_col))
        return -1


        