class Solution:
    def dfs(self, i, path):
        if len(path) > self.k:
            return
        if len(path) == self.k:
            self.output.append(path)
        for i in range(i, self.n):
            self.dfs(i+1, path+[i+1])

    def combine(self, n, k):
        self.output = []
        self.n = n
        self.k = k
        self.dfs(0, [])
        return self.output

    def combine2(self, n: int, k: int) -> list[list[int]]:
        """
        given n, k,
        return all possible combinations of k numbers
        chosen from the range [1,n]
        easy O(n^2) solution
        """
        output, temp = [], []
        def backtrack(n, k, num):
            if len(temp) == k:
                output.append(temp.copy())
            for i in range(num, n+1):
                temp.append(i)
                backtrack(n,k,i+1)
                temp.pop()
        backtrack(n,k,1)
        return output

q = Solution()
print(q.combine(4,3))
