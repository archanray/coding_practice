class Solution:
    def removeZeroSumSublists(self, nums):
        """
        Leetcode - 1171
        Given a list remove sublists that sum to zero
        """
        prefixSum = 0
        dictOfSums = {}
        for i in range(len(nums)):
            prefixSum += nums[i]
            dictOfSums[prefixSum] = i
            
        # if element is repeated in the prefixSum then there is a sublist which sums to 0 or repeats
        dropIDs = []
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if dictOfSums[prefixSum] != i:
                dropIDs = list(set(dropIDs).union(set(range(i+1, dictOfSums[prefixSum]+1))))
                i = dictOfSums[prefixSum]+1
                
        return dropIDs

inputs = [1,2,3,-3,-2]
q = Solution()
print(q.removeZeroSumSublists(inputs))