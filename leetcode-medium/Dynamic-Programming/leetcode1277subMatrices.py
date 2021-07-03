"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ansMatrix = [[0]*(m+1) for _ in range(n+1)]
        print(ansMatrix)
        count = 0
        for row in range(1, n+1):
            print(row, "i am row")
            for col in range(1, m+1):
                print(col, "i am col")
                if matrix[row-1][col-1]==1:
                    ansMatrix[row][col]=1+min(ansMatrix[row][col-1],ansMatrix[row-1][col], ansMatrix[row-1][col-1])
                    count += ansMatrix[row][col]
        return count