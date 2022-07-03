"""
https://leetcode.com/problems/sparse-matrix-multiplication/submissions/
311. Sparse Matrix Multiplication
"""


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if mat1 == [[0]]: return [[0]]
        ans = []
        matrixC = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row_index, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                if row_element:
                    for col_index, col_element in enumerate(mat2[element_index]):
                        matrixC[row_index][col_index] += col_element * row_element
        return matrixC
