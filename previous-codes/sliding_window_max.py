# return max element of sliding window
# input: list of integers, window size
# output: list of max elements of each window
# required runtime: O(n)

import collections
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        ans = []                # List to store the maximum values for each sliding window
        q = collections.deque()  # Deque to store indices of elements in the current window
        left = right = 0         # Pointers for the sliding window

        while right < len(nums):
            # Pop smaller values from the back of the deque
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # Remove the leftmost value if it's outside the current window
            if left > q[0]:
                q.popleft()

            # If the window size is reached, append the maximum value to the result
            if (right + 1) >= k:
                ans.append(nums[q[0]])
                left += 1
            right += 1

        return ans
    def unOptimizedMaxSlidingWindow(self, nums, k):
        if not nums:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        maxes = []
        for i in range(len(nums) - k + 1):
            maxes.append(max(nums[i:i+k]))
        return maxes

inputs = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
print(s.maxSlidingWindow(inputs, k)) # [3,3,5,5,6,7]