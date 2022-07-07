"""
https://leetcode.com/problems/toeplitz-matrix/
766. Toeplitz Matrix
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        myHash = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row - col not in myHash:
                    myHash[row - col] = matrix[row][col]
                elif myHash[row - col] != matrix[row][col]:
                    return False
        return True


"""
What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
[[1,2,3,4],
[5,1,2,3],
[9,5,1,2]]
We go top down:
Step 1: load First row 1, 2, 3, 4
Step 2: 4 is valid so move col 3 pointer forward since thats valid 1, 2 , 3, 3;
Step 3: 3 & 3 are valid so move col 2 and col 3 : 1, 2, 2, 2;
Step 4: 2 & 2 & 2 are valid so move col 1, 2, 3 : 1 , 1, 1, null; (drop col 3);
Step 5: 1 & 1 & 1 are valid so move col 0, 1, 2: 5, 5, null, null (drop col 2);
Step 6: 5 & 5 are valid so move col 0, 1: 9, null (drop col 1);
Step 7: 9 is valid;

return valid;
"""
