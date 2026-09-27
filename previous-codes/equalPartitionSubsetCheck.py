# Link: https://leetcode.com/problems/partition-equal-subset-sum/
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
class Solution:
    def canPartition(self, nums):
        """assuming nums are all integers"""
        total_sum = sum(nums)
        # if total_sum is odd, return False
        if total_sum % 2:
            return False
        # if total_sum is even, we can find a subset that sums to total_sum//2
        subset_sum = total_sum // 2
        # dp[i] is True if there is a subset of nums that sums to i
        dp = [False] * (subset_sum + 1)
        # base case: there is a subset that sums to 0
        dp[0] = True
        # for each number in nums, update dp
        for num in nums:
            # for each sum from subset_sum to num, update dp
            for _sum in reversed(range(num, subset_sum+1)):
                # if there is a subset that sums to _sum-num or there is a subset that sums to _sum
                # then there is a subset that sums to _sum
                dp[_sum] = dp[_sum] or dp[_sum-num]
                # if there is a subset that sums to subset_sum, return True
                if dp[subset_sum]:
                    return dp[subset_sum]
        return dp[subset_sum]

# test cases
# input = [1,5,11,5]
# output: True
# input = [1,2,3,5]
# output: False
# input = [1,2,5]
# output: False

inputs = [1,5,11,5]
q = Solution()
print("Resultant subsets:", q.canPartition(inputs))