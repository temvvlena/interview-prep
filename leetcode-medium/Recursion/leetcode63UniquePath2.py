class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        if obstacleGrid[0][0]==1: return 0
        obstacleGrid[0][0]=1
        
        for col in range(1, len(obstacleGrid)):
            obstacleGrid[col][0] = int(obstacleGrid[col][0] == 0 and obstacleGrid[col-1][0] == 1)
            
        for row in range(1, len(obstacleGrid[0])):
            obstacleGrid[0][row] = int(obstacleGrid[0][row] == 0 and obstacleGrid[0][row-1] == 1)     
            
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]