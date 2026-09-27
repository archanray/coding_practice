class Solution():
    def binSearch(self, target, left):
        # arr is a sorted array
        # target is the target to be searched
        right = self.n-1
        while left <= right:
            mid = left + (right - left) // 2
            if self.nums[mid] == target:
                return mid
            if self.nums[mid] < target:
                left = left+1
            else:
                right = right-1
        return -1
    def countSameTriplet(self, nums):
        """
        Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

        Input: 
        N = 4 
        arr[] = {1, 5, 3, 2}
        Output: 2 
        Explanation: There are 2 triplets:
        1 + 2 = 3 and 3 +2 = 5

        Input: 
        N = 3
        arr[] = {2, 3, 4}
        Output: 0
        Explanation: No such triplet exits
        
        This code runs in O(n^2 log n) time and requires O(1) space in theory
        # implemented as a list, so triplets can be 3^n
        """
        self.nums = sorted(nums)
        self.n = len(nums)
        triplets = []
        count = 0
        for i in range(0, self.n):
            for j in range(i+1, self.n):
                q = self.binSearch(self.nums[i]+self.nums[j], j+1)
                if not q == -1:
                    triplets.append([self.nums[i], self.nums[j], self.nums[q]])
                    count += 1
        return triplets, count
    
    def targetSum(self, target, lastID):
        # find two elements from sorted array that matches the target
        l = 0
        r = lastID
        while l < r:
            if self.nums[l] + self.nums[r] == target:
                return l, r
            if self.nums[l] + self.nums[r] < target:
                l = l+1
            else:
                r = r-1
        return -1, -1
    
    def findTriplet(self, nums):
        """
        solves the above problem in O(n^2) time
        
        # solution:
        1. sort array
        2. go from right to left
        3. for each element, set as target and solve target sum in O(n) time
        """
        self.nums = sorted(nums)
        n = len(nums)
        
        triplets = []
        count = 0
        for i in range(n-1,-1,-1):
            l, r = self.targetSum(self.nums[i], i-1)
            if not l == -1 or not r == -1:
                triplets.append([self.nums[l], self.nums[r], self.nums[i]])
                count += 1
        return triplets, count

arr = [5, 32, 1, 7, 10, 50, 19, 21, 2]
q = Solution()
print(q.countSameTriplet(arr))
print(q.findTriplet(arr))
