# Question: find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# LC: medium
class Solution():
	def minimumTotal(self, a):
		depth = len(a)
		if depth == 1:
			return a[0][0]

		DP = [[0]*(depth+1) for _ in range(depth+1)]
		
		for level in range(depth-1, -1, -1):
			for i in range(level+1):
				DP[level][i] = a[level][i] + \
				min(DP[level+1][i], DP[level+1][i+1])

		return DP[0][0]

q = Solution()
print(q.minimumTotal([[-1],[2,3],[1,-1,-3]]))
