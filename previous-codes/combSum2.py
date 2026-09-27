class Solution:
    def dfsTarget(self, idx, path, sumNow):
        if sumNow > self.target:
            return
        if sumNow == self.target:
            self.output.append(path)
            return
        # now actually loop through the values
        for i in range(idx, self.n):
            if i > idx and self.candidates[i] == self.candidates[i-1]:
                continue
            val = self.candidates[i]
            self.dfsTarget(i+1, path+[val], sumNow+val)

    def combSumTarget(self, candidates, target):
        self.output = []
        self.candidates = sorted(candidates)
        self.target = target
        self.n = len(self.candidates)
        self.dfsTarget(0, [], 0)
        return self.output


    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def dfs(idx, path, cur):
            if cur > target:
                return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        dfs(0,[],0)
        return res

q = Solution()
print(q.combinationSum2([10,1,2,7,6,1,5], 8))
print(q.combSumTarget([10,1,2,7,6,1,5], 8))
print(q.combinationSum2([2,5,2,1,2], 5))
print(q.combSumTarget([2,5,2,1,2], 5))