# Given an unsorted integer array nums, return the smallest missing positive integer.
class Solution:
    def firstMissingPositive(self, nums):
        nums = [i for i in nums if i > 0]
        nums.sort()
        if not nums:
            return 1
        if nums[0] != 1:
            return 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1
        return nums[-1] + 1
# Time complexity: O(nlogn)
# Space complexity: O(1)
nums = [1,2,0]
q = Solution()
print(q.firstMissingPositive(nums)) # 3