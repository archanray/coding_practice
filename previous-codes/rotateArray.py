class Solution(object):
    def rotateOn(self, nums, k):
        """
        O(n) space rotate
        """
        n = len(nums)
        q = nums[n-k:]+nums[0:n-k]
        nums = q

    def rotate(self, nums, k):
        """
        in-place rotate
        """
        n = len(nums)
        for i in range(k):
            nums.insert(0, nums[n-1])
            nums.pop()
        return nums

q = Solution()
print(q.rotate([1,2,3,4,5,6,7], 3))
