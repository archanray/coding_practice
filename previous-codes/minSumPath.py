# no diagonal moves are allowed
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        saveMat = []
        for i in range(n):
            rows = [0 for j in range(m)]
            saveMat.append(rows)
        saveMat[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    saveMat[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    saveMat[i][j] = saveMat[i][j-1] + grid[i][j]
                elif  i > 0 and j == 0:
                    saveMat[i][j] = saveMat[i-1][j] + grid[i][j]
                else:
                    saveMat[i][j] = min(saveMat[i-1][j] + grid[i][j],\
                                        saveMat[i][j-1] + grid[i][j])
        return saveMat[-1][-1]

q = Solution()
print(q.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

print(q.minPathSum([[1,2,3],[4,5,6]]))