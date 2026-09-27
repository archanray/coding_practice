class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for left in range(n-1, -1, -1):
            dp[left][left] = 1
            for right in range(left+1, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left+1][right-1]+2
                else:
                    dp[left][right] = max(dp[left+1][right], dp[left][right-1])
        return dp[0][n-1]

inputs = "cbbd"
q = Solution()
print(q.longestPalindromeSubseq(inputs))