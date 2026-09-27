class Solution:
    def dfs(self, start, path, res):
        res.append(path)
        for i in range(start, len(self.nums)):
            if i>start and self.nums[i] == self.nums[i-1]:
                continue
            # print(path+[self.nums[i]], res)
            self.dfs(i+1, path+[self.nums[i]], res)

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # first sort the list
        nums = sorted(nums)
        self.nums = nums
        self.out = []
        self.dfs(0, [], self.out)
        
        return self.out

q = Solution()
print(q.subsetsWithDup([1,2,3]))
