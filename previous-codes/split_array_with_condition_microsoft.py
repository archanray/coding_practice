class Solution:
    def computeSums(self, nums):
        n = len(nums)
        leftSums = [0] * n
        rightSums = [0] * n
        leftSums[0] = nums[0]
        for i in range(1,n):
            leftSums[i] = leftSums[i-1] + nums[i]
        for j in range(n-2,-1,-1):
            rightSums[j] = rightSums[j+1] + nums[j+1]
        return leftSums, rightSums
    def solution(self, nums1, nums2):
        if len(nums1) != len(nums2):
            return -1
        n = len(nums1)
        if n <= 1:
            return 0
        LS1, RS1 = self.computeSums(nums1)
        LS2, RS2 = self.computeSums(nums2)
        count = 0
        for i in range(n-1):
            if LS1[i] == RS1[i] and LS2[i] == RS2[i]:
                count += 1
        return count

inputs1 = [20,10,13,14,15,5,2,3,14,3]
inputs2 = [20,10,13,14,15,5,2,3,14,3]
print(Solution().solution(inputs1, inputs2))