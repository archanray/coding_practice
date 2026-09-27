class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        """
        given input create a spiral matrix of size nxn
        """
        output = [[0]*n for i in range(n)]
        i = 0
        start_col, start_row = 0,0
        end_col, end_row = n,n

        while start_col < end_col or start_row < end_row:
            for c in range(start_col, end_col):
                i += 1
                output[start_row][c] = i
            start_row += 1
            for r in range(start_row, end_row):
                i += 1
                output[r][end_col-1] = i
            end_col -= 1
            for c in range(end_col-1, start_col-1,-1):
                i += 1
                output[end_row-1][c] = i
            end_row -= 1
            for r in range(end_row-1,start_row-1,-1):
                i += 1
                output[r][start_col] = i
            start_col += 1
        return output

q = Solution()
print(q.generateMatrix(5))
