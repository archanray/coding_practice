class Solution():
	def dfs(self, idx, path, sumNow):
		if sumNow > self.target and len(path) <= self.minlen:
			self.minlen = len(path)
			self.output.append(path)
			return
		for i in range(idx, self.n):
			if i > idx and self.nums[i] == self.nums[i-1]:
				continue
			q = self.nums[i]
			self.dfs(i+1, path+[q], sumNow+q)
	def findSmallestSubArray(self, nums, target):
		self.output = []
		self.nums = sorted(nums)
		self.target = target
		self.n = len(nums)
		self.nums = nums
		self.minlen = self.n+1
		self.dfs(0, [], 0)
		# self.output is also a good output
		print(self.output)
		if self.minlen == self.n+1:
			return None
		return self.minlen

q = Solution()
print(q.findSmallestSubArray([1, 4, 45, 6, 0, 19], 51))