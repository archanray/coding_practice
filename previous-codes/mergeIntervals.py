class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        # sorting uses O(n log n)
        intervals = sorted(intervals)

        merged = []

        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)

        return merged

q = Solution()
print(q.merge([[1,3],[2,6],[8,10],[15,18]]))
print(q.merge([[1,4],[4,5]]))