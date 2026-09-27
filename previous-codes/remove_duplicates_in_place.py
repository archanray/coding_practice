class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        general idea: 
        1. start from index 1
		2. if index i == index i-1:
		2a. if counter == 0 increase counter and move on to next index
		2b. if counter == 1 remove the element, decrease size of size,
		but keep index as as the next element is now the current element
		3. if everything fails, then ith element is different than i-1th
		element. Since the list is sorted, set counter to 0 and set i=i+1
        """
        n = len(nums)
        counter = 0
        i = 1
        while i < n:
            if nums[i] == nums[i-1] and counter == 0:
                counter += 1
                i = i+1
                continue
            if nums[i] == nums[i-1] and counter == 1:
                nums.remove(nums[i])
                n = n-1
                continue
            counter = 0
            i = i+1
            