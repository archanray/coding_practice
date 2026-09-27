class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        product of all number except self
        using O(n) time and without using division
        """
        n = len(nums)
        outputs = [0]*n
        prefixProduct = 1
        suffixProduct = 1

        for i in range(n):
            outputs[i] = prefixProduct
            prefixProduct *= nums[i]
        for i in range(n-1,-1,-1):
            outputs[i] *= suffixProduct
            suffixProduct *= nums[i]
        return outputs