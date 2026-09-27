class Solution():
    def findDuplicate(self, nums):
        # floyd's tortoise and hare algorithm
        tortoise, hare = nums[0], nums[0]

        # move tortoise and hare until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # reset tortoise to the start of the list
        tortoise = nums[0]

        # move tortoise and hare at the same speed until they meet again
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        # return the duplicate number
        return tortoise

vals = [3,1,3,4,2]
q = Solution()
print(q.findDuplicate(vals))