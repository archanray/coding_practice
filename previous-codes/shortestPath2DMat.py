class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        try to go from 0,0 to m,n
        using BFS
        """
        if grid == [[0]]:
            return 1
        if grid[0][0] or grid [-1][-1]:
            return -1
        m,n = len(grid), len(grid[0])
        
        # init x, y, path_lengths
        q = [(0,0,1)]
        # mark init as visited
        grid[0][0] = 1

        # now go solve!
        # while something is in q
        while len(q) >= 1:
            x, y, PL = q.pop(0)

            # check all neighbors
            # variations in chess board: changes these accordingly
            # to find immediate neighbors
            for xs in [x-1,x,x+1]:
                for ys in [y-1, y, y+1]:
                    # condition for final index
                    if xs == n-1 and ys == m-1:
                        return PL + 1

                    # else find where to next
                    if 0 <= xs and xs < n and 0 <= ys and ys < m:
                        # can only move through 0s
                        if grid[xs][ys] == 0:
                            q.append((xs, ys, PL+1))
                            grid[xs][ys] = 1
        return -1

q = Solution()
print(q.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))       