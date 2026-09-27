# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
# this is just an alternate version of interval merging
# we can use the same approach as in merge_intervals.py
class Solution:
    def employeeFreeTime(self, schedule):
        intervals = []
        for emp in schedule:
            for start, end in emp:
                # adding start end as a tuple
                intervals.append((start, end))
        # sort the tuple intervals
        intervals.sort()
        res = []
        # prev is the end of the first interval
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            # if start is greater than prev, append the interval
            if start > prev:
                res.append([prev, start])
            # update prev to be the max of prev and end
            prev = max(prev, end)
        return res
# Time complexity: O(nlogn)
# Space complexity: O(n)
schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
q = Solution()
print(q.employeeFreeTime(schedule)) # [[5,6],[7,9]]