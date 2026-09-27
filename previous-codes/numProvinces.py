# LC: medium
from collections import deque
class Solution():
    def dfs(self, start):
        if self.visited[start] == 0:
            self.visited[start] = 1
            for j in range(self.n):
                if self.isConnected[start][j] == 1:
                    self.dfs(j)
    def findCircleNum(self, isConnected):
        # finding connected components in a graph
        self.isConnected = isConnected
        self.n = len(isConnected)
        self.visited = [0 for _ in range(self.n)]
        if self.n == 0:
            return 0
        count = 0
        for i in range(self.n):
            if self.visited[i] == 0:
                # print(i, self.visited)
                self.dfs(i)
                count += 1
        return count

    def neighbors8(self, x, y):
        outputs = []
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                if 0 <= i < self.m:
                    neighborX = i
                else:
                    continue
                if 0 <= j < self.n:
                    neighborY = j
                else:
                    continue
                outputs.append([neighborX, neighborY])   
        return outputs
    
    def neighbors4(self, x, y):
        check = [[x-1, y], [x+1, y], [x,y-1], [x,y+1]]
        outputs = []
        for neighbor in range(len(check)):
            if 0<= check[neighbor][0] < self.m and 0<= check[neighbor][1] < self.n:
                outputs.append(check[neighbor])
        return outputs
                    
    def BFS(self, grid, x, y):
        queue = deque([])
        queue.append([x, y])
        while queue:
            x, y = queue.popleft()
            neighborsOfTop = self.neighbors4(x, y)
            for neighbor in neighborsOfTop:
                dx, dy = neighbor[0], neighbor[1]
                if self.visited[dx][dy] == 0 and grid[dx][dy] == "1":
                    queue.append([dx, dy])
                else:
                    self.visited[dx][dy] = 1
            self.visited[x][y] = 1
        
    def numIslands(self, grid):
        self.isConnected = grid
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[0 for _ in range(self.n)] for _ in range(self.m)]
        if self.n == 0:
            return 0
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.visited[i][j] == 0 and grid[i][j] == "1":
                    self.BFS(grid, i, j)
                    count += 1
                else:
                    continue
        return count

inputs = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
q = Solution()
print(q.numIslands(inputs))