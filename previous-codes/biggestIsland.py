class Solution():
    def path(self, i, j):
        if i > 0 and j > 0:
            path = [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]
        if i > 0 and j == 0:
            path = [[i-1,j], [i+1,j], [i,j+1]]
        if i == 0 and j > 0:
            path = [[i+1,j], [i,j-1], [i,j+1]]
        if i == 0 and j == 0:
            path = [[i,j+1], [i+1,j]]
        finalPath = []
        for i,j in path:
            print(i, j)
            if i < self.m and j < self.n:
                finalPath.append([i,j])
        return finalPath
    def BFS(self, start):
        i, j = start[0], start[1]
        stackNodes = []
        stackNodes.append((i,j))
        val = 0
        self.visited[i][j] = 1
        val += 1
        while stackNodes != []:
            i,j = stackNodes.pop()
            for q,r in self.path(i,j):
                if self.grid[q][r] == 1 and self.visited[q][r] == 0:
                    stackNodes.append((q, r))
                    self.visited[q][r] = 1
                    val += 1
        return val
    def maxAreaOfIsland(self, grid):
        # 4-sided connectivity
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            if grid[0][0] == 1:
                return 1
            else:
                return 0
        maxVal = 0
        self.m, self.n = m, n
        self.grid = grid
        self.visited = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1 and self.visited[i][j] == 0:
                    start = [i,j]
                    maxVal = max(maxVal,self.BFS(start))
        return maxVal

inputGrid = [[0],[1]]
q = Solution()
print(q.maxAreaOfIsland(inputGrid))