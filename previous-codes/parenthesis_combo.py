class Solution:
    def putIn(self, res, left, right, s, n):
        """
        just do a dfs!
          """
        if len(s) == n*2:
            res.append(s)
            return res
        if left < n:
            res = self.putIn(res, left+1, right, s+"(", n)
        if right < left:
            res = self.putIn(res, left, right+1, s+")", n)
        return res
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        res = self.putIn(res, 0, 0, "", n)
        return res

q = Solution()
print(q.generateParenthesis(1))
print(q.generateParenthesis(2))
print(q.generateParenthesis(3))