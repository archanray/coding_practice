class Solution:
	def preprocessor(self, str1: str) -> list:
		j = 0
		n = len(str1)
		lookup = [0 for x in range(n)]
		i = j+1
		while i < n:
			if str1[i] == str1[j]:
				j = j+1
				lookup[i] = j
				i = i+1
			else:
				if j != 0:
					j = lookup[j-1]
				else:
					lookup[i] = 0
					i = i+1
		return lookup

	def KMPsolver(self, str1: str, str2: str) -> list:
		lookup = self.preprocessor(str2)
		i, j = 0, 0
		n, m = len(str1), len(str2)
		while i < n and j < m:
			if str1[i] == str2[j]:
				i, j = i+1, j+1
				if j == m:
					return "Match found! See back from index: "+str(i-1)
			else:
				if j != 0:
					j = lookup[j-1]
				else:
					i = i+1
		return "No match found"

q = Solution()
print(q.KMPsolver("abxabcabcaby", "abcaby"))
print(q.KMPsolver("abczxabcdabxabcdabcdabcy", "abcdabca"))
print(q.KMPsolver("abcxabcdabxabcdabcdabcy", "aabaabaaa"))
print(q.KMPsolver("aabaabaabaabaabaabaab", "aaab"))
print(q.KMPsolver("parabola", "abo"))
print(q.preprocessor("abcdabedabf"))