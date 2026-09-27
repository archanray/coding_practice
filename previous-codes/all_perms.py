from copy import copy
class Solution:
    def fact(self, num):
        factorial = 1
        for i in range(num):
            factorial *= num
            num = num-1
        return factorial
    def nextPermutation(self, nums1) -> list[int]:
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
        nums = copy(nums1)
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

        # this is returned if the last permutation is observed
        nums.reverse()
        return nums

    def permute_using_fact(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        # print(n)
        nf = self.fact(n)
        list_perms = []
        list_perms.append(nums)
        # print(list_perms)
        for i in range(nf-1):
            # print(list_perms)
            nums = self.nextPermutation(nums)
            # print(nums)
            if nums is None:
                return list_perms
            elif nums in list_perms:
                pass
            else:
                list_perms.append(nums)
        return list_perms
    
    def backtrack(self):
        n = len(self.nums)
        if len(self.p) == n:
            self.ans.append(self.p[:])
            return
        for i in range(n):
            if not self.v[i]:
                self.v[i] = True
                self.p.append(self.nums[i])
                self.backtrack()
                self.v[i] = False
                self.p.pop()
        return
    def permute(self, nums):
        self.ans = []
        self.p = []
        self.v = [False] * len(nums)
        self.nums = nums
        self.backtrack()
        return self.ans

q = Solution()
print(len(q.permute([1,-2,1,-2,1,-2])))