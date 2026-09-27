# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# algorithm logic:
# 1. Create a function to check if the current position is valid.
# 2. Create a function to solve the n-queens puzzle.
# 3. Create a variable to store the result.
# 4. Call the solve function.
# 5. Return the result.
# time complexity: O(n!)
# space complexity: O(n)
class Solution:
    def solveNQueens(self, n):
        def is_valid(board, x, y):
            for i in range(x):
                if board[i] == y or abs(x - i) == abs(y - board[i]):
                    return False
            return True
        def dfs(board, x):
            if x == n:
                res.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in board])
                return
            for i in range(n):
                if is_valid(board, x, i):
                    board[x] = i
                    dfs(board, x + 1)
                    board[x] = -1
        res = []
        dfs([-1] * n, 0)
        return res

n = 4
q = Solution()
print(q.solveNQueens(n)) # [['.Q..','...Q','Q...','..Q.'],['..Q.','Q...','...Q','.Q..']]