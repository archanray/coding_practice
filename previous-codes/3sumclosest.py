class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort() # O(n log n)
        res = []

        max_dist = 2*10**4
        max_sum = 0
        for i, a in enumerate(nums):
            #print(i,a)
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r] - target
                if abs(threeSum) < max_dist:
                    max_dist = abs(threeSum)
                    max_sum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append((a, nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return max_sum

q = Solution()

print(q.threeSumClosest([-1,2,1,-4], 1))