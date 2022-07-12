"""
https://leetcode.com/problems/set-matrix-zeroes/
Set Matrix Zeroes
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Time Complexity O(N^3) and will do Squared soon
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    r.add(row)
                    c.add(col)
        """
        r = {1}
        c = {1}
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in r or col in c: matrix[row][col]=0

"""
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][col] = "0"
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    matrix[row][col] = 0 
                    for i in range(len(matrix[0])):
                        if matrix[row][i] != "0":
                            matrix[row][i] = 0
                    for i in range(len(matrix)):
                        if matrix[i][col] != "0":
                            matrix[i][col] = 0
"""