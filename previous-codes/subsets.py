# LC: medium
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set). The solution set must not contain duplicate 
        subsets. Return the solution in any order.
        """
        # setting up output with the empty element
        output = [[]]
        n = len(nums)
        for i in range(n):
            counter = 0
            output_len = len(output)
            for subset in output:
                new_subset = subset + [nums[i]]
                output.append(new_subset)
                counter += 1
                if counter >= output_len:
                    break
        return output

