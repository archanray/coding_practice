class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        return subarray with maxiumum sum
        naive solution:
        for each start position i and end position j:
            store the sum
        output the max value in the nxn matrix
        but this takes O(n^2) time!
        """
        """
        using Kadence for O(n) algorithm
        max_A[i] = max(A[i], A[i]+max_A[i-1])
        """
        global_max = -float("inf")
        local_max = 0
        n = len(nums)
        for i in range(n):
            local_max = max(nums[i], nums[i]+local_max)
            if local_max >= global_max:
                global_max = local_max
        return global_max

q = Solution()
print(q.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(q.maxSubArray([5,4,-1,7,8]))