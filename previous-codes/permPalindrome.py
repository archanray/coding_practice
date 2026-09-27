class Solution():
	def permPalindrome(self, string):
		if len(string) < 2:
			return True
		dictionary = {}
		n = len(string)
		for i in range(n):
			if string[i] not in dictionary.keys():
				dictionary[string[i]] = 1
			else:
				if dictionary[string[i]] == 1:
					dictionary[string[i]] = 0
				else:
					dictionary[string[i]] = 1

		counter = 0
		for key in dictionary.keys():
			if dictionary[key] == 1:
				counter += 1
		if counter == 1 or counter == 0:
			return True
		else:
			return False

q = Solution()
string = "abab"
print(q.permPalindrome(string))