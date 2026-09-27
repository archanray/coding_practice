class Solution():
	def alphabet(self):
		"""
		this returns the alphabet
		"""
		abc = "abcdefghijklmnopqrstuvwxyz"
		abc = list(abc)
		return abc

	def pangramChecker(self, strings):
		"""
		given list of strings return if they are pangrams

		answer format: "1100" for 4 strings with first 2
		being pangrams and last 2 being not
		"""
		m = len(strings)
		output = ""
		for i in range(m):
			abc = self.alphabet()
			n = 26
			for j in range(n):
				if abc[i] in strings[i]:
					abc.remove(abc[i])
			if len(abc) == 0:
				output += "1"
			else:
				output += "0"
		return output

q = Solution()
print(q.pangramChecker(["the quick brown fox jumps over the lazy dog", "the quick     brown", "hello world"]))

