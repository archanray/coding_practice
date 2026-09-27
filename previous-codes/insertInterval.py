class Solution:
    def mergeIntervals(self, intervals):
        # key assumption: the list is sorted by the start index
        # runs in O(n)
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
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # the input is sorted!

        # insert the new interval in the right spot
        # then run the merge interval subroutine
        # runs in O(n)+mergeIntervals time
        if len(intervals) == 0:
            return [newInterval]
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[0] <= interval[0]:
                intervals.insert(i, newInterval)
                break
            if i == len(intervals) - 1:
                intervals.append(newInterval)
        # print(intervals)
        intervals = self.mergeIntervals(intervals)
        return intervals

q = Solution()
print(q.insert([[1,5]], [2,7]))
        