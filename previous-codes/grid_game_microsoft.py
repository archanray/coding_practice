class Solution:
    def gridGame(self, grid):
        upperRight, lowerLeft, result = sum(grid[0]), 0, float("inf")
        for upperVal, lowerVal in zip(grid[0], grid[1]):
            upperRight -= upperVal
            result = min(result, max(upperRight, lowerLeft))
            lowerLeft += lowerVal
        return result
    
input = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
print(Solution().gridGame(input))