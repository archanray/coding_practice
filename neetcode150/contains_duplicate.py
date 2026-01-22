
class Solution:
    def hasDuplicateSort(self, nums: list[int]) -> bool:
        """
        Time complexity: O(nlog n), Space complexity O(1) or O(n)
        """
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    def hasDuplicateSet(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n), Space complexity: O(n)
        """
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False
    def hasDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
    
q = Solution()
print(q.hasDuplicate([-1,0,1,2,-2,-4]))