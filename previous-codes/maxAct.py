class Solution():
	def activityCount(self, start, finish):
		# time stamps given
		# finish time is sorted
		# if not sorted, sort the finish time and rearrage starts
		m, n = len(start), len(finish)
		ids = []
		if m == 0 or n == 0:
			return ids
		ids.append(0)
		ET = finish[0]
		for i in range(1,m):
			if start[i] < ET:
				pass
			else:
				ET = finish[i]
				ids.append(i)

		return ids

q = Solution()
print(q.activityCount([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))