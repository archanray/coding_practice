class Solution:
    def numberOfWeeks(self, milestones):
        sumval, maxval = sum(milestones), max(milestones)
        if sumval - maxval >= maxval:
            return sumval
        return 2*(sumval-maxval) + 1
        