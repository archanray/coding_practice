class Solution:
    def lengthOfCLIS(self, nums):
        """
        length of contiguous subsequence of increasing sequence
        """
        maxLength = 0
        localLength = 0
        for i in range(len(nums)):
            if i == 0:
                localLength += 1
                maxLength += 1
            elif nums[i] > nums[i-1]:
                localLength +=1
                maxLength = max(maxLength, localLength)
            else:
                localLength = 1
        return maxLength
    
    def lengthOfLIS(self, nums):
        """
        problem 300
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        

input = [10,9,2,5,3,7,101,18]
q = Solution()
print(q.lengthOfLIS(input))