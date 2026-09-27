class Solution():
	def fibonacci(self, num):
		"""
		takes input of num
		returns fibonacci number corresponding to num
		"""
		if num == 1 or num == 0:
			return num
		
		return self.fibonacci(num-1)+self.fibonacci(num-2)

	def mainFibonacci(self, num):
		"""
		takes length num and return finacci series of size num
		"""
		sequence = []
		for i in range(num+1):
			sequence.append(self.fibonacci(i))
		return sequence

q = Solution()
print(q.mainFibonacci(20))