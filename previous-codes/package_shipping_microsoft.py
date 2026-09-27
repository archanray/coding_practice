class Solution:
    def shipWithinDays(self, weights, days):
        maxWeight = max(weights)
        totalWeight = sum(weights)
        left, right = maxWeight, totalWeight
        while left < right:
            mid = (left+right) // 2
            daysNeeded, currentWeight = 1, 0
            for weight in weights:
                if currentWeight + weight > mid:
                    daysNeeded += 1
                    currentWeight = 0
                currentWeight += weight
            if daysNeeded > days:
                left = mid+1
            else:
                right = mid
        return left