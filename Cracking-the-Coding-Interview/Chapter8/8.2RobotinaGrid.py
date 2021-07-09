"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to 
the bottom right.
"""

def findPath(myList):
    print(myList, "Before")
    m = len(myList)
    n = len(myList[0])
    # Edge case
    if myList[0][0] == 1: return 0
    myList[0][0] = 1
    # First make the first col equal to 1 if there's no obstacles
    for col in range(1, m):
        myList[col][0] = int(myList[col][0] == 0 and myList[col-1][0] == 1)
    
    # Second make the first row equal to 1 if there's no obstacles
    for row in range(1, n):
        myList[0][row] = int(myList[0][row] == 0 and myList[0][row-1]==1)
    
    for i in range(1, m):
        for j in range(1, n):
            if myList[i][j] == 0:
                myList[i][j] = myList[i-1][j]+myList[i][j-1]
            else:
                myList[i][j] = 0

    print(myList, "After")        
    return myList[m-1][n-1]  

print(findPath([[0,0,0],[0,1,0],[0,0,0]])) # Return 2
print(findPath([[0,0]])) # Return 1 
print(findPath([[0,1],[0,0]])) # Return 1
