class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        Bellman-Ford
        """
        cost = [10**6] * n
        cost[src] = 0
        for i in range(k + 1):
            tempCost = cost.copy()
            for s, d, c in flights:
                if cost[s] == 10**6:
                    continue
                if cost[s] + c < tempCost[d]:
                    tempCost[d] = cost[s] + c
            cost = tempCost
        if cost[dst] == 10**6:
            return -1
        return cost[dst]