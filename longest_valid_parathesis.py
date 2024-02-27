#Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

input = "(()"
q = Solution()
print(q.longestValidParentheses(input)) #Output: 2