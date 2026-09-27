class Solution:
    def longestArithSeqLength(self, nums):
        # nums = sorted(nums) # do this to find only increasing subsequences
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][0] = 1
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff not in dp[j]:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff]+1
            ans = max(ans, max(dp[i].values()))
        return ans
    
    def numberOfArithmeticSlices(self, nums):
        total_count = 0
        n = len(nums)
        dp = [{} for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_j = dp[j].get(diff, 0)
                count_i = dp[i].get(diff, 0)
                dp[i][diff] = count_i + count_j + 1
                total_count += count_j
            
        return total_count

# [4, 7, 1, 5, 3]
# [12, 12, 12, 15, 10]
# [18, 26, 18, 24, 24, 20, 22]
nums = [18, 26, 18, 24, 24, 20, 22]
print(Solution().numberOfArithmeticSlices(nums))