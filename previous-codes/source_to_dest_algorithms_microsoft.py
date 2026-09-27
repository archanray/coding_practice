from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def buildGraph(self, times):
        graph = defaultdict(list)
        for city_from, city_to, weight in times:
            graph[city_from-1].append((city_to-1, weight))
        return graph
    def networkDelayTimeDjikstra(self, times, n, k):
        # times[i] = (ui, vi, wi)
        # total nodes n
        # start node k
        ## use djikstra tto find shortest path from node[k] to all nodes
        
        # construct directed graph as a dictionary
        graph = self.buildGraph(times)
        visited  = [False for _ in range(n)]
        distance = [float("inf") for _ in range(n)]
        # put cost, index to the queue
        queue = [(0,k-1)]
        distance[k-1] = 0
        while queue:
            current_cost, current_city = heappop(queue)
            visited[current_city] = True
            for next_city, next_cost in graph[current_city]:
                if visited[next_city] == False and distance[next_city] > current_cost+next_cost:
                    distance[next_city] = current_cost+next_cost
                    heappush(queue, (current_cost+next_cost, next_city))
        print(visited, distance)
        if max(distance) < float("inf"):
            return max(distance)
        else:
            return -1
    
    def networkDelayTimeBellmanFord(self, times, n, k):
        ## this function uses Bellman Ford
        
        # initialize graph
        # graph = self.buildGraph(times)
        k=k-1
        distance = [float("inf") for _ in range(n)]
        predecessor = [None for _ in range(n)]
        distance[k] = 0
        
        # relax edges repeatedly
        for i in range(n-1):
            for u,v,w in times:
                u, v = u-1, v-1
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
        
        # check for negative weight cycles
        for u,v,w in times:
            u, v = u-1, v-1
            if distance[u] + w < distance[v]:
                predecessor[v] = u
                # negative cycle exists, find vertex on cycle
                visited = [False for i in range(n)]
                visited[v] = True
                while not visited[u]:
                    visited[u] = True
                    u = predecessor[u]
                # u is a vertex in the negaive cycle
                ncycle = [u]
                v = predecessor[u]
                while v!=u:
                    ncycle = ncycle+[v]
                    v = predecessor[v]
                print("Graph containst negative cycle:", ncycle)
        if max(distance) < float("inf"):
            return max(distance)
        else: 
            return -1

    def networkDelayTimeFloydWarshall(self, times, n, k):
        ## this function uses Floyd Warshall (all pair shortest path)
        query = k-1
        distances = [[float("inf") for i in range(n)] for i in range(n)]
        for u,v,w in times:
            u, v = u-1, v-1
            distances[u][v] = w
        for u in range(n):
            distances[u][u] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
        candidates = distances[query][:]
        print(distances)
        if max(candidates) < float("inf"):
            return max(candidates)
        else: 
            return -1
    
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTimeFloydWarshall(times, n, k))