class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        general idea:
        1. find elements where the first low element is met with high element
        (to do this go from right to left)
        2. Once found, sort all the elements following this
        3. then swap the clashed element with the immediate larger element
        in the sorted sublist
        """
        for i in range(len(nums)-1, 0, -1):
            # find the index of the last element which is big
            if nums[i-1] < nums[i]:
                nums[i:] = sorted(nums[i:])
            # find index of mismatch
            j = i-1

            # put the pre-last value with the value just larger than it
            for k in range(i, len(nums)):
                if nums[j] < nums[k]:
                    nums[k], nums[j] = nums[j], nums[k]
                    return nums

        # this is returned is the last permutation is observed
        return nums.reverse()

q = Solution()
print(q.nextPermutation([1,3,2]))