class Solution:
    def carFleet(self, target, position, speed):
        # sort the cars as per distance and speed
        sortedCars = sorted(zip(position, speed),reverse=True)
        bottleneck = float("-inf")
        fleet = 0
        
        for d,s in sortedCars:
            remainingDist = target-d
            timeToReachTarget = remainingDist / s
            
            if timeToReachTarget > bottleneck:
                bottleneck = timeToReachTarget
                fleet += 1
        return fleet
    
inputs1 = 5
inputs2 = [0,2,4]
inputs3 = [4,2,1]
print(Solution().carFleet(inputs1, inputs2, inputs3))