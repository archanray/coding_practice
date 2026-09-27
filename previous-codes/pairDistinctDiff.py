class Solution():
    def binSearch(self, k, index):
        # log n time binary search
        if self.n <= 1:
            return -1
        
        left, right = index, self.n-1
        while left <= right:
            mid = left + (right - left) // 2
            if self.nums[mid] == k:
                return True
            if self.nums[mid] < k:
                left = mid+1
            if self.nums[mid] > k:
                right = mid-1
        return False

    def countPairsWithDiffK(self, nums, k):
        # idea binary search for each number!
        # n log n total complexity
        self.n = len(nums)
        if self.n <= 1:
            return 0

        nums = sorted(nums)
        self.nums = nums

        count = 0
        for i in range(self.n):
            query = self.nums[i]+k
            if self.binSearch(query, i):
                count += 1
        return count

numbers = [8, 12, 16, 4, 0, 20]
diff = 4
q = Solution()
print(q.countPairsWithDiffK(numbers, diff))