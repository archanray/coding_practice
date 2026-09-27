class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxarea = 0
        while left < right:
            areahere = min(height[left], height[right]) * (right - left)
            maxarea = max(maxarea, areahere)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
            
        return maxarea


q = Solution()
print(q.maxArea([1,8,6,2,5,4,8,3,7]))

print(q.maxArea([1,1]))

print(q.maxArea([1,2,1]))