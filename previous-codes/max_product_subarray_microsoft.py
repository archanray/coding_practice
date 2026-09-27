class Solution:
    def maxProduct(self, nums):
        # trying modified kadane
        # maxVal = max(A[i-1]+nums[i], nums[i])
        n = len(nums)
        res = nums[0]
        currMax, currMin = 1, 1
        for n in nums:
            vals = (n, n*currMax, n*currMin)
            currMax, currMin = max(vals), min(vals)
            res = max(res, currMax)
        return res
    
    