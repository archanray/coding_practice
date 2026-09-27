#Given an m x n integers matrix, return the length of the longest increasing path in matrix.
class Solution:
    def dfs(self, i, j):
        if self.cache[i][j]:
            return self.cache[i][j]
        for dx, dy in self.dirs:
            x, y = i+dx, j+dy
            if 0 <= x < self.m and 0 <= y < self.n and self.matrix[x][y] > self.matrix[i][j]:
                self.cache[i][j] = max(self.cache[i][j], self.dfs(x, y))
        self.cache[i][j] += 1
        return self.cache[i][j]
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cache = [[0] * n for _ in range(m)]
        self.m, self.n = m, n
        self.dirs = dirs
        self.cache = cache
        self.matrix = matrix
        return max(self.dfs(i, j) for i in range(m) for j in range(n))
#Time complexity: O(m*n)

input = [[9,9,4],[6,6,8],[2,1,1]]
q = Solution()
print(q.longestIncreasingPath(input)) #Output: 4