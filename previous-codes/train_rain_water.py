class Solution:
    def trap(self, heights):
        # Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
        # The idea is to find the maximum height of a bar from the left and right for each index and the amount of water that can be stored on that index is the minimum of the two heights minus the height of the current index.
        # The total amount of water that can be trapped is the sum of the amount of water that can be trapped on each index.
        n = len(heights)
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] = heights[0]
        right_max[n-1] = heights[n-1]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], heights[i])
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], heights[i])
        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - heights[i]
        return total_water
    
input = [0,1,0,2,1,0,1,3,2,1,2,1]
q = Solution()
print(q.trap(input)) # 6