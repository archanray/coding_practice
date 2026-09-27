# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
import collections
class Solution:
    def numBusesToDestination(self, routes, source, target):
        # if we are exactly at the target, return 0
        if source == target:
            return 0
        # create a dictionary of stops to routes
        stop_to_routes = collections.defaultdict(set)
        # for each route, add the stops to the dictionary
        for i, route in enumerate(routes):
            # for each stop in the route, add the route to the set of routes for that stop
            for stop in route:
                # add the route to the set of routes for that stop
                stop_to_routes[stop].add(i)
        # create a visited set and a queue
        visited = set()
        # add the source to the queue
        queue = collections.deque([(source, 0)])
        # while the queue is not empty
        while queue:
            # pop the leftmost element from the queue
            stop, buses = queue.popleft()
            # if the stop is the target, return the number of buses
            if stop == target:
                # return the number of buses
                return buses
            # for each route in the set of routes for the stop
            for route in stop_to_routes[stop]:
                # if the route has been visited, continue
                if route in visited:
                    continue
                # add the route to the visited set
                visited.add(route)
                # for each stop in the route
                for next_stop in routes[route]:
                    # if the stop has not been visited
                    if next_stop != stop:
                        # add the stop to the queue
                        queue.append((next_stop, buses + 1))
        # if the queue is empty, return -1
        return -1

inputs = [[1,2,7],[3,6,7]]
source = 1
target = 6
s = Solution()
print(s.numBusesToDestination(inputs, source, target)) # 2