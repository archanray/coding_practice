class Solution:
	def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
		nums.sort()
		res = []
		n = len(nums)

		for i in range(n):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			for j in range(i+1,n):
				if j > i+1 and nums[j] == nums[j-1]:
					continue
				# solve twoSums here
				l, r = j+1, n-1
				while l < r:
					fourSums = nums[i] + nums[j] + nums[l] + nums[r]
					if fourSums < target:
						l += 1
					elif fourSums > target:
						r -= 1
					else:
						res.append([nums[i], nums[j], nums[l], nums[r]])
						l+=1
						while l<r and nums[l] == nums[l-1]:
							l+=1
		return res

q = Solution()

print(q.fourSum([1,0,-1,0,-2,2], 0))

print(q.fourSum([2,2,2,2,2], 8))


