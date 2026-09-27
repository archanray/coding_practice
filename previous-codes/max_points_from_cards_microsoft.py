class Solution:
    def maxScore(self, nums, k):
        n = len(nums)
        totalSum = sum(nums)
        remainingLength = n-k
        subarraySum = sum(nums[:remainingLength])
        minSum = subarraySum
        
        for i in range(remainingLength, n):
            # update sliding window sum to subarray sum ending at i
            subarraySum += nums[i]
            subarraySum -= nums[i - remainingLength]
            #  update minSum to track overall minSum
            minSum = min(minSum, subarraySum)
            
        return totalSum - minSum
    
    def maxScore(self, arr, k):
        # my code
        # Create two arrays to store the cumulative sum of the left and right parts
        left_sums = [0] # left to right sum
        right_sums = [0] # right to left sum
        
        n = len(arr)
        
        # Compute the cumulative sum of the left and right parts
        for i in range(k):
            left_sums.append(arr[i] + left_sums[-1])
            right_sums.append(arr[n-1-i] + right_sums[-1])
        
        # Find the maximum score by summing the values of the left and right parts for each possible split
        max_score = 0
        for i in range(k+1):
            score = left_sums[i] + right_sums[k-i]
            max_score = max(max_score, score)
        
        return max_score