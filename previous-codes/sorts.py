class Solution():
    def partition(self, nums, lo, hi):
        # find middle of the array
        pivot = hi

        i = lo

        for j in range(lo, hi):
            if nums[j] < nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i
        
    def quicksort(self, nums, lo, hi):
        # print(nums)
        if lo < hi:
            pivot = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, pivot-1)
            self.quicksort(nums, pivot+1, hi)
        return
    def mergeSort(self, nums):
        n = len(nums)
        if n > 1:
            mid = n // 2

            L = nums[:mid]
            R = nums[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i,j,k = 0,0,0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i+=1
                else:
                    nums[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                nums[k] = L[i]
                k+=1
                i+=1
            while j < len(R):
                nums[k] = R[j]
                j+=1
                k+=1

    def sortArray(self, nums):
        n = len(nums)
        # self.quicksort(nums, 0, n-1)
        self.mergeSort(nums)
        return nums

q = Solution()
print(q.sortArray([8,1,-1,20, 13, 12, 1]))