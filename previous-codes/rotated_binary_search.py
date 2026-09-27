class Solution(object):
    def searchPeak(self,nums):
        """
        find index of max element and return index in log n
        """
        n=len(nums)
        left, right = 0, n-1
        if n == 0:
            return -1
        if n == 1:
            return 0

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] <= nums[left]:
                right = mid
            else:
                left = mid

        return mid

    def binSearch(self, arr, target):
        """
        binary search
        """
        # base checks
        # print(arr)
        n = len(arr)
        left, right = 0, n-1
        if n == 0:
            return -1
        if n == 1:
            if arr[0] == target:
                return 0
            else:
                return -1

        # actual search
        while left <= right:
            mid = left+(right-left)//2
            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                left = mid+1
            if arr[mid] > target:
                right = mid-1

        return -1


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int (position)
        """
        # get the mid value
        peakID = self.searchPeak(nums)

        # check where you'd want to run binary search!
        if nums[0] <= target <= nums[peakID]:
            return self.binSearch(nums[:peakID+1], target)
        else:
            b = self.binSearch(nums[peakID+1:], target)
        if b == -1:
            return b
        else:
            return b+peakID+1

q = Solution()
print(q.search([4,5,6,7,8,1,2,3], 1))
# print(q.search([4,5,6,7,0,1,2], 3))
# print(q.search([6,7,1,2,3,4,5], 6))
# print(q.search([2], 3))
# print(q.search([4,5,6,7,0,1,2], 0))