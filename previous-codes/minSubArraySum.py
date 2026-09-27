# LC: medium
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        return sub array with smallest length equalling sum
        guaranteed to have the target as a sub array (sub arrays are continuous)
        """
        if sum(nums) < target:
            return 0
        total, left, output = 0, 0, len(nums)

        for right, value in enumerate(nums):
            total += value
            while total >= target:
                total -= nums[left]
                output = min(output, right-left+1)
                left += 1
        return output

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(s.minSubArrayLen(4, [1,4,4])) # 1
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0
print(s.minSubArrayLen(11, [1,2,3,4,5])) # 3
print(s.minSubArrayLen(15, [1,2,3,4,5])) # 5
print(s.minSubArrayLen(100, [2,3,1,2,4,3])) # 0