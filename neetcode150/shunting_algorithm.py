from collections import deque

class Solution:
    def shunt(self, tokens: list[str]) -> int:
        """
        assumes that the input is tokenized
        """
        precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}  
        right_assoc = {'^'}
        stack = []
        queue = deque()

        return None

q = Solution()
tokens = ["3", "+", "4", "*", "2", "/", "(", "1", "−", "5", ")", "^", "2", "^", "3"]
print(q.shunt(tokens))