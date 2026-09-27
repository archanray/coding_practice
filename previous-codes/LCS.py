class Solution:
	def LCS(self, word1:str, word2:str) -> int:
		"""
		compute longest common subsequence
		"""
		C = []
		n = len(word1)
		m = len(word2)
		# set the matrix to all 0s
		for i in range(n+1):
			rows = [0 for x in range(m+1)]
			C.append(rows)
		for i in range(n+1):
			C[i][0] = 0
		for j in range(m+1):
			C[0][j] = 0
		for i in range(1,n+1):
			for j in range(1,m+1):
				if word1[i-1] == word2[j-1]:
					C[i][j] = C[i-1][j-1] + 1
				else:
					C[i][j] = max(C[i][j-1], C[i-1][j])
		return C[n][m]

q = Solution()
print(q.LCS("AGGTAB", "GXTXAYB"))
print(q.LCS("BD", "ABCD"))
print(q.LCS("AXYT", "AYZX"))
print(q.LCS("BACDB", "BDCB"))