class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        gas: amount of gas at station i
        cost: cost to go from ith to (i+1)th station

        return:
        starting index such that you can go clockwise once
        else:
        return -1
        """
        if sum(gas) - sum(cost) < 0:
            return -1
        n = len(gas)
        leftOver = 0
        location = n+1

        for i in range(n):
            leftOver += gas[i] - cost[i]
            if leftOver < 0:
                leftOver = 0
                location = n+1
            else:
                location = min(i, location)
        return location

