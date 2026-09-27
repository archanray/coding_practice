from heapq import heappush, heappop
class Solution:
    def neighbors8(self, x, y):
        neighbors = []
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                if 0<=i<self.m and 0<=j<self.n and self.visited[i][j] == False and self.grid[i][j] > 0:
                    neighbors.append([i,j])
        print("neighbors", x, y, neighbors)
        return neighbors
        
    def highestRankedKItemsPQ(self, grid, pricing, start, k):
        # grid is the actual store grid
        # pricing is the range
        # start is the start cell
        # k are the top items to store
        queue = [start]
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        vals = []
        while queue:
            print("Queue:", queue)
            cell = queue.pop()
            x, y = cell[0], cell[1]
            print("Queue pop:", x, y)
            if grid[x][y] == 1:
                self.visited[x][y] = True
                for neighbor in self.neighbors8(x, y):
                    queue.append(neighbor)
            else:
                if pricing[0] <= grid[x][y] <= pricing[1] and self.visited[x][y] == False:
                    heappush(vals, (-grid[x][y], x, y))
                    self.visited[x][y] = True
                else:
                    continue
            # print(queue, self.visited)
            # self.visited[x][y] = True
            print("Candidates:", vals)
        outputs = []
        while k > 0 and vals:
            # print(vals, outputs)
            value, dx, dy = heappop(vals)
            print(value, dx, dy)
            outputs.append([dx, dy])
            k -= 1
        if k > 0:
            return -1
        return outputs[::-1]
    
    def highestRankedKItems(self, grid, pricing, start, k):
        m, n = len(grid), len(grid[0])
        sx, sy = start
        pl, ph = pricing
        q = [(0, grid[sx][sy], sx, sy)]
        visited = set()
        res = []

        while q:
            dis, price, x, y = heappop(q)
            if (x, y) in visited: continue
            
            visited.add((x, y))
            
            if price != 1 and pl <= price <= ph: 
                res.append([x, y])
            if len(res) == k: 
                return res

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    val = grid[new_x][new_y]
                    if val == 0: 
                        continue
                    else: 
                        heappush(q, (dis + 1, val, new_x, new_y))
        return res

grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
pricing = [2,3]
start = [2,3]
k = 2
print(Solution().highestRankedKItems(grid, pricing, start, k))