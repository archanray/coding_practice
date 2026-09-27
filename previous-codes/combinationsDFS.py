class Solution():
    def dfs(self, root, others, tmp):
        tmp.append(root)
        if len(tmp) == self.k:
            self.output.append(tmp)
            return

        for i in range(len(others)):
            self.dfs(others[i], others[i+1:], tmp[:])

    def combinations(self, n, k):
        self.candidates = list(range(1,n+1))
        self.output = []
        self.k = k
        for i in range(n):
            self.dfs(self.candidates[i], self.candidates[i+1:], [])
        return self.output

q = Solution()
print(q.combinations(4, 2))