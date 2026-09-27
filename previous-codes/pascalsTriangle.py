class Solution():
    def factorial(self, num):
        val = 1
        while num > 0:
            val = val*num
            num = num-1
        return val
    def countCombinations(self, n, p):
        if n < p:
            return -1
        div = self.factorial(n-p) * self.factorial(p)
        val = self.factorial(n) / div
        return val
    def pascals(self, lines):
        Q = []
        for i in range(lines):
            localList = []
            for j in range(i+1):
                localList.append(self.countCombinations(i, j))
            Q.append(localList)
        return Q

lines = 10
q = Solution()
print(q.pascals(lines))
