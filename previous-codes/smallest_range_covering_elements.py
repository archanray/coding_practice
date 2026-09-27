# Find the smallest range that includes at least one number from each of the k lists.
class Solution:
    def smallestRange(self, nums):
        import heapq
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        ans = -1e9, 1e9
        right = max(row[0] for row in nums)
        while heap:
            left, i, j = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(heap, (v, i, j + 1))
        return ans
# Time complexity: O(nlogk)
# Space complexity: O(k)
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
q = Solution()
print(q.smallestRange(nums)) # [20,24]
    