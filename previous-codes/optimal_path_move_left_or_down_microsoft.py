class Solution:
    def solution(self, grid):
        n = len(grid[0])
        if n == 0:
            return -1
        if n == 1:
            return grid[0][0] + grid[1][0]
        prefixArray = [0] * (n)
        suffixArray = [0] * (n)
        prefixArray[0] = grid[0][0]
        suffixArray[n-1] = grid[1][n-1]
        for i in range(1, n):
            prefixArray[i] = prefixArray[i-1] + grid[0][i]
        for j in range(n-2,-1,-1):
            suffixArray[j] = suffixArray[j+1] + grid[1][j]
        result = float("inf")
        swapNode = -1
        for i in range(n):
            query = prefixArray[i] + suffixArray[i]
            if query <= result:
                result = query
                swapNode = i
        return result, swapNode

input = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
print(Solution().solution(input))
            