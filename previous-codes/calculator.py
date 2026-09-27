# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        res = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res

input = "1 + 1"
q = Solution()
print(q.calculate(input))