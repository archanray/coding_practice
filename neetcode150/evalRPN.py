import operator
class Solution:
    """
    evaluate RPN expressions
    time compelxity is O(n)
    space complexity is O(n)
    """
    def truncated_div(self, a, b):
        return int(operator.truediv(a, b))
    def evalRPN(self, tokens: list[int]) -> int:
        stackvals = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": self.truncated_div,
        }
        for i in range(len(tokens)):
            if tokens[i] in ops:
                a = stackvals.pop()
                b = stackvals.pop()
                stackvals.append(ops[tokens[i]](b, a))
            else:
                stackvals.append(int(tokens[i]))
        return stackvals[-1]

q = Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(q.evalRPN(tokens))