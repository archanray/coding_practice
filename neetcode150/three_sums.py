from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
        
            l, r  = i+1, len(nums)-1
            while l < r:
                threeSums = a + nums[l] + nums[r]
                if threeSums < target:
                    l += 1
                elif threeSums > target:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res