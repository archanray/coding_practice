class Solution:
    def nonConseqSum(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        a, b, c = dp[0], dp[1], 0
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            c = max(b, a+nums[i])
            a = b
            b = c
            c = 0
        return dp[-1], b

inputs = [10,5,5,35]
q = Solution()
print(q.nonConseqSum(inputs))