# Write a program to solve a Sudoku puzzle by filling the empty cells.
class Solution:
    def solveSudoku(self, board):
        def is_valid(x, y, val):
            for i in range(9):
                if board[x][i] == val or board[i][y] == val:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3)*3+i][(y//3)*3+j] == val:
                        return False
            return True
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if is_valid(i, j, str(k)):
                                board[i][j] = str(k)
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        solve()
        
input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
q = Solution()
q.solveSudoku(input)
print(input)