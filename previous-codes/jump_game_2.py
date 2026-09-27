class Solution:
    def jump(self, nums: list[int]) -> int:
        end = 0
        max_reach = 0
        count = 0
        nmo = len(nums)-1

        # BFS
        for i in range(nmo):
            max_reach = max(max_reach, i+nums[i])
            if max_reach >= nmo:
                count += 1
                return count
            if i == end:
                count += 1
                end = max_reach
        return count
q = Solution()
print(q.jump([2,3,1,1,4]))
print(q.jump([2,3,0,1,4]))
print(q.jump([1,2]))