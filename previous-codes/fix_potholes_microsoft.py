class Solution:
    def solution(self, s, B):
        # the algo is O(nlog n) because of the sort
        nums = []
        val = 0
        flag = False
        for i in range(len(s)):
            if s[i] == ".":
                if val > 0:
                    nums.append(val)
                    val = 0
                flag = True
            else:
                val = val + 1
                flag = False
        if flag == False:
            nums.append(val)
        # sort the numbers:
        nums = sorted(nums)
        # print(nums)
        
        # complete largest jobs first
        count = 0
        ID = len(nums) - 1
        while B > 1 and ID >= 0:
            if B-nums[ID]-1 >= 0:
                ID -= 1
                count += nums[ID]
                B = B-nums[ID]-1
            else:
                count = count + max(0, B-1)
                B = 0
                ID-=1
        return count
    
# "...xxx..x....xxx.", 7
# "..xxxxx", 4
# "x.x.xxx...x", 14
# "..", 5;

input1, input2 = "..", 5
print(Solution().solution(input1, input2))