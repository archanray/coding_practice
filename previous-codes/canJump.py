class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        from any position see where you can reach.
        if you cant improve reach and 
        your id is less than max reach return false
        else continue
        if total reach is geq final element
        return true
        if for loop end return false
        compute current_reach as i+nums[i]
        max_reach = max(max_reach, current_reach)
        """
        if len(nums) == 1:
            return True
        max_reach = 0
        nmo = len(nums)-1
        for i in range(nmo):
            current_reach = nums[i]+i
            if max_reach == current_reach and i >= current_reach:
                return False
            max_reach = max(max_reach, current_reach)
            if max_reach >= nmo:
                return True
            # print(i, max_reach, current_reach)
        return False
            
q = Solution()
print(q.canJump([2,1,2,2,1,2,2,2]))