class Solution:
    def mysearch(self, nums: list[int], target: int) -> int:
        """
        straight forward binary search
        O(log n)
        """
        n = len(nums)
        if n == 0:
            return -1
        current_index = n//2
        left = 0
        right = n
        while nums[current_index] != target and right - left > 1:
            print("enter index:", current_index)
            if nums[current_index] > target:
                right = current_index
                current_index = left + (right - left) // 2
            else:
                left = current_index
                current_index = current_index + (right - left) // 2
            print("exit index:", current_index)
        if right-left <= 1 and nums[current_index] != target:
            return -1
        else:
            return current_index

    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = n = len(nums)
        while left < right:
            middle = left + ((right-left)//2)
            if nums[middle] >= target:
                right = middle
            else:
                left = middle+1
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1

q = Solution()
nums=[-1,0,3,5,9,12]
target=9
print(q.search(nums, target))