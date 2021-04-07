"""
Given an image represented by an N x N matrix, where each pixel in the image 
is represented by an integer, write a method to rotate the image by 90 degrees.
Can you do this in place?

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Input: matrix = [[1]]
Output: [[1]]

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

def rotate(matrix):  
    print("Before rotation", matrix)
    """  
    def rotate-1(self, matrix: List[List[int]]) -> None:
        def swapFunction(row, col, length):
            # 0, 1 ---> row = 0, col = 1
            temp = matrix[row][col] # 2
            matrix[row][col]=matrix[length-col-1][row] # matrix[5-1-1][0]
            matrix[length-col-1][row]=matrix[length-1-row][length-col-1] # matrix[5-1-1][0]  -1, 3;  -1, -2
            matrix[length-1-row][length-col-1]=matrix[col][length-row-1]   #1, -1,         
            matrix[col][length-row-1]=temp 
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-1-i):    
                swapFunction(i, j, len(matrix))
    """  
    # Diagnol swap
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i] = temp 
    # Column Swap
    for i in range(len(matrix)):
        for j in range(len(matrix)//2):
            temp = matrix[i][j]
            matrix[i][j]=matrix[i][len(matrix)-j-1]
            matrix[i][len(matrix)-j-1]=temp
    print("Rotated 90 degree", matrix)

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))