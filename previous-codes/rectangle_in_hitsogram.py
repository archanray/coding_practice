# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

input = [2,1,5,6,2,3]
q = Solution()
print(q.largestRectangleArea(input)) #Output: 10