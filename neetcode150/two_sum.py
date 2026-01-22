from copy import copy
class Solution:
    def twoSumSort(self, nums: list[int], target: int) -> list[int]:
        """
        exactly one pair matches target, O(nlog n)
        """
        sortednums = copy(nums)
        sortednums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            TS = sortednums[l] + sortednums[r]
            if TS == target:
                break
            if TS < target: 
                l += 1
            else:
                r -= 1 
        first_index = nums.index(sortednums[l])
        
        for index, item in enumerate(nums):
            """
            this is O(n)
            """
            if (item == sortednums[r]) and (not index == first_index):
                returnVal = [first_index, index]
                returnVal.sort()
                return returnVal
        return None
    def twoSums(self, nums: list[int], target: int) -> list[int]:
        """
        use hashmap to do this.
        """
        return None
q = Solution()
print(q.twoSum(nums=[-1,-2,-3,-4,-5], target=-8))