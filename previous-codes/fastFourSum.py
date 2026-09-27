class Solution():
    def hashmap(self, nums):
        hashMap = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = nums[i]+nums[j]
                if target in hashMap.keys():
                    if sorted([nums[i],nums[j]]) not in hashMap[target]:
                        hashMap[target].append(sorted([nums[i],nums[j]]))
                else:
                    hashMap[target] = [sorted([nums[i],nums[j]])]
        return hashMap

    def findPartner(self, nums, a, lo, hi):
        if hi < lo:
            return -float("inf")

        mid = (hi-lo) // 2 + lo

        if nums[mid] + a == 0:
            return nums[mid]
        if nums[mid] + a <= 0:
            return self.findPartner(nums, a, mid+1, hi)
        else:
            return self.findPartner(nums, a, lo, mid-1)

    def twoSums(self, nums, target):
        n = len(nums)
        nums = sorted(nums)
        limit = -float("inf")
        for i in range(len(nums)):
            b = self.findPartner(nums, nums[i]-target, i+1, n)
            if b != limit:
                return b
            else:
                return limit


    def fourSums(self, nums, target):
        if len(nums) <= 3:
            return "no combinations found"
        hashMap = self.hashmap(nums)
        matches = self.twoSums(hashMap.keys(), target)



q = Solution()
print(q.fourSums([9, 8, 7, 2, 0, 4, 1, 1, 6, 2], 9))