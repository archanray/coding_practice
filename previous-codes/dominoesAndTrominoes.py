class Solution:
    def numTilings(self, n):
        """
        You have two types of tiles: a 2 x 1 domino shape 
        and a tromino shape. You may rotate these shapes.
        Given an integer n, return the number of ways to 
        tile an 2 x n board. Since the answer may be very 
        large, return it modulo 10e9 + 7.

        In a tiling, every square must be covered by a tile. 
        Two tilings are different if and only if there are 
        two 4-directionally adjacent cells on the board such 
        that exactly one of the tilings has both squares 
        occupied by a tile.
        """
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        self.mod = 1e9 + 7
        sols = [0] * (n+1)
        sols[0] = 1
        sols[1] = 1
        sols[2] = 2
        sols[3] = 5
        # A = single domino
        # B = stacked dominoes
        # C = L7 or T_|
        # sols 3 is constructed as:
        # =, =|, |=, L7, T_| (with Ls), observe the new tiles
        # for sol 4:
        # sol[1] + C (2, for 2 combinations), 
        # sols[2] + B (2), 
        # sols[3] + A (5),
        # and a new set of blocks as TT or L_| (2, 2 new combinations). 
        # so sols[n] = sols[n-1] + A, sol[n-2] + B, sols[n-3] + C
        # sols[n] = sols[n-1]*1 + sols[n-2]*1 + \sum_{i=0 to N-3}sols[i]*2
        # sols[n] = sols[n-1] + sols[n-2] + 2\sum_{i=0 to N-3}sols[i]
        # sols[n] = sols[n-1] + sols[n-2] + sols[n-3] + sols[n-3] + 2\sum_{i=0 to N-4}sols[i]
        # sols[n] = sols[n-1] + sols[n-3] + (sols[n-2] + sols[n-3] + 2\sum_{i=0 to N-4}sols[i])
        # sols[n] = sols[n-1] + sols[n-3] + sols[n-1] (note the bracket portion is sols[n-1])
        # that's it!
        for i in range(4,n+1):
            sols[i] = int((2*sols[i-1] + sols[i-3]) % self.mod)
        return sols[n]

inputs = 1
q= Solution()
print(q.numTilings(inputs))