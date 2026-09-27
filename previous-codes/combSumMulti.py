class Solution():
    def dfs(self, idx, path, sumNow):
        if sumNow > self.target:
            return
        if sumNow == self.target:
            self.output.append(path)
        for i in range(idx, self.n):
            v = self.nums[i]
            self.dfs(i, path+[v], sumNow+v)

    def matchTarget(self, nums, target):
        # return unique combinations
        self.target = target
        self.nums = nums
        self.n = len(self.nums)
        self.output = []
        self.count = 0
        self.dfs(0,[],0)
        # returns unique paths to the sum
        # to get all can do permutation which can be cheaper
        return self.output

    def combinationSum4(self, nums, target):
        DP = [0]*(target+1)
        DP[0] = 1
        for i in range(target+1):
            for num in nums:
                if i >= num:
                    DP[i] = DP[i] + DP[i-num]
        return DP[target]


if __name__ == "__main__":
    candidates = [1,2,3]
    toReach = 4
    q = Solution()
    print(q.matchTarget(candidates, toReach))
    print(q.combinationSum4(candidates, toReach))