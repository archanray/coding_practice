class Solution:
    def getNextStop(self, nums, ID, direction):
        if ID == -1:
            # -1 indices means out of bounds
            return -1
        elif (nums[ID] > 0) != direction:
            # check if direction is same
            return -1
        next_ID = (ID + nums[ID]) % len(nums)
        if next_ID == ID:
            return -1
        return next_ID
        
    def circularArrayLoop(self, nums):
        # find if there is a cycle in a nums
        # naive solution: run starting from each index. This will take O(n^2) time
        # solution: use slow and fast pointers
        n = len(nums)
        visited = [0] * n
        for i in range(n):
            fast  = i
            slow = i
            
            direction = nums[i] > 0
            
            while True:
                slow = self.getNextStop(nums, slow, direction)
                # tmp fast used for making fast go 2X speed of slow
                tmp_fast = self.getNextStop(nums, fast, direction)
                fast = self.getNextStop(nums, tmp_fast, direction)
                
                if slow == -1 or fast == -1:
                    break
                elif slow == fast:
                    return True
        return False

query = [1,-1,5,1,4]
q = Solution()
print(q.circularArrayLoop(query))