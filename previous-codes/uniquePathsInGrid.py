class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        Number of unique paths from 0,0 to m-1,n-1
        Grid of size mxn
        Allowed to move down or right only!

        DP:
        path to each cell: 
        2: top and left
        1: if row or column number is 0

        recursion:
        A[i,j] = A[i-1,j] + A[i,j-1]
        """
        # set up the DP matrix mxn
        DP = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    DP[i][j] = 1
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        paths from top left to bottom right avoiding the obstacle
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        DP = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = 0
                elif i == 0 and j == 0:
                    DP[i][j] = 1
                else:
                    if obstacleGrid[i-1][j] == 1:
                        DP[i][j] = DP[i][j-1]
                    elif obstacleGrid[i][j-1] == 1:
                        DP[i][j] = DP[i-1][j]
                    else:
                        DP[i][j] = DP[i][j-1]+DP[i-1][j]
        return DP[m-1][n-1]


q = Solution()
# print(q.uniquePaths(3,7))
# print(q.uniquePaths(3,2))
print(q.uniquePathsWithObstacles([[0,1]]))