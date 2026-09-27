class Solution():
	def binSearch(self, arr, target):
		# log n search 
		left, right = 0, self.n-1
		while left <= right:
			mid = left+ (right-left) // 2
			if arr[mid] == target:
				return mid
			else:
				if arr[mid] < target:
					left = mid+1
				else:
					right = mid-1
		return -1
	def findPairs(self, arr1, arr2, target):
		# O(n log n) code to find pairs of numbers matching a target
		output = []
		m = len(arr1)
		self.n = len(arr2)
		if m == 0 or self.n == 0:
			return output

		arr1 = sorted(arr1)
		arr2 = sorted(arr2)
		for i in range(m):
			q = self.binSearch(arr2, target-arr1[i]) 
			if q != -1:
				output.append([arr1[i], arr2[q]])
		return output

q = Solution()
print(q.findPairs([1, 2, 4, 5, 7], [5, 6, 3, 4, 8], 9))