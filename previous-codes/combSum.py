class Solution:
    def dfs(self, idx, targetSum, path):
        if targetSum < 0:
            return
        if targetSum == 0:
            self.output.append(path)
            return
        for i in range(idx, self.n):
            q = self.candidates[i]
            # set call index as i if reapts are allowed, else do i+1
            self.dfs(i, targetSum - q, path+[q])

    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.n = len(self.candidates)
        self.output = []
        self.dfs(0, target, [])
        return self.output

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        self.dfs(candidates, target, [], result)
        return result

    def dfs2(self, nums, target, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], result)



q = Solution()
print(q.combinationSum([2,3,6,7], 7))