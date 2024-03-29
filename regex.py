class Solution():
	def isMatch(self, s, p):
		# "." means any combinations will match
		# "*" any of the previous characters can be used to match
		# we will use dynamic programming
		m, n = len(s), len(p)
		dp = [[False]*(n+1) for _ in range(m+1)]
		dp[0][0] = True
		for j in range(1, n+1):
			if p[j-1] == "*":
				dp[0][j] = dp[0][j-2]
			else:
				dp[0][j] = j > 1 and p[j-1] == "*" and dp[0][j-2]

		for i in range(1, m+1):
			for j in range(1, n+1):
				if p[j-1] == s[i-1] or p[j-1] == ".":
					dp[i][j] = dp[i-1][j-1]
				elif p[j-1] == "*":
					dp[i][j] = dp[i][j-2] or \
							   (p[j-2] == s[i-1] or p[j-2] == ".")\
							   and dp[i-1][j]
				else:
					dp[i][j] = False
		return dp[m][n]