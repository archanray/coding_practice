class Solution(object):
    def binSearch(self, A, target):
        """
        binary search for a target number
        """
        # base cases
        n = len(A)
        left, right = 0, n-1
        if n == 0:
            return -1
        if n == 1:
            if A[0] == target:
                return 0
            else:
                return -1

        # find elements
        while left <= right:
            mid = left + (right-left)//2
            if A[mid] == target:
                return mid

            if A[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # base cases
        n = len(nums)
        left, right = 0, n-1
        if n == 0:
            return [-1, -1]
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        oneID = self.binSearch(nums, target)
        if oneID != -1:
            # now search around the ID to find the low and high
            j=oneID
            while j >= 0 and nums[j] == nums[oneID]:
                j = j-1
            j = j+1
            k = oneID
            while k < n and nums[k] == nums[oneID]:
                k = k+1
            k = k-1
            return [j,k]

        return [-1,-1]

q = Solution()
print(q.searchRange([5,7,7,8,8,8,10], 8))
print(q.searchRange([2,2], 2))