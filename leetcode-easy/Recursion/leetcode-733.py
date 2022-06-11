"""
https://leetcode.com/problems/flood-fill/
Flood Fill
"""


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):

        def dfs(image, row, col, newColor, temp):
            if image[row][col] == temp:
                image[row][col] = newColor
                if len(image) - 1 > row:
                    dfs(image, row + 1, col, newColor, temp)
                if row >= 1:
                    dfs(image, row - 1, col, newColor, temp)
                if len(image[0]) - 1 > col:
                    dfs(image, row, col + 1, newColor, temp)
                if col >= 1:
                    dfs(image, row, col - 1, newColor, temp)

        temp = image[sr][sc]
        if temp == newColor: return image
        dfs(image, sr, sc, newColor, temp)

        return image
