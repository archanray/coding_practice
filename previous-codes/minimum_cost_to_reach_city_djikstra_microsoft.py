# import sys
# class Solution:
#     def minDist(self, dist, visited):
#         minDist = sys.maxsize
#         for u in range(self.V):
#             if dist[u] < minDist and visited[u] == False:
#                 minDist = dist[u]
#                 minIndex = u
#         return minIndex
#     def minimumCost(self, n, highways):
#         # true djikstra, only for no discounts
#         self.V = n
#         # create adjacency matrix
#         G = [[0 for col in range(n)] for row in range(n)]
#         for e in highways:
#             u, v, w = e[0], e[1], e[2]
#             G[u][v] = w
#             G[v][u] = w
#         # start djikstra
#         dist = [sys.maxsize] * n
#         dist[0] = 0
#         visited = [False] * n
#         for count in range(n):
#             x = self.minDist(dist, visited)
#             print(x)
#             visited[x] = True
#             for y in range(self.V):
#                 if G[x][y] > 0 and visited[y] == False and dist[y] > dist[x] + G[x][y]:
#                     dist[y] = dist[x]+G[x][y]
#             print(dist, visited)
#         if visited[-1] == True:
#             return dist[-1]
#         else:
#             return -1
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minimumCost(self, cities, highways, discounts):
        # Create a graph to store city connections and costs
        graph = defaultdict(list)
        for city_from, city_to, cost in highways:
            graph[city_from].append((city_to, cost))
            graph[city_to].append((city_from, cost))
      
        # Initialize a priority queue with starting point information
        # (cost to reach city, current city, current number of discounts used)
        queue = [(0, 0, 0)]
      
        # Initialize distance table to keep track of the minimum cost with varying number of discounts applied
        distance = [[float('inf')] * (discounts + 1) for _ in range(cities)]
      
        # Continue until the queue is empty
        while queue:
            # Dequeue the next (cost, current city, discounts used)
            current_cost, current_city, used_discounts = heappop(queue)
          
            # Ignore paths where we've exceeded the number of discounts available
            if used_discounts > discounts:
                continue
          
            # Check if we've reached the destination with this path
            if current_city == cities - 1:
                return current_cost
          
            # If this is the best cost for this city with this number of used discounts, update it
            if distance[current_city][used_discounts] > current_cost:
                distance[current_city][used_discounts] = current_cost
              
                # Explore paths from the current city
                for next_city, next_cost in graph[current_city]:
                    # Add path to the same city with no discount used
                    heappush(queue, (current_cost + next_cost, next_city, used_discounts))
                    # Add path to the same city with a discount, if we have any left
                    if used_discounts < discounts:
                        heappush(queue, (current_cost + next_cost // 2, next_city, used_discounts + 1))
      
        # If the destination city was not reached return -1
        return -1


n = 4 #5 # 4
highways = [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]] #[[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]] #[[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]]
discounts = 20 #1 #20
print(Solution().minimumCost(n, highways, discounts))