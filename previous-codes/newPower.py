class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        my implementation of power function
        using bitwise operation
        complexity: O(log n)
        """
        if n < 0:
            sign = -1
        else:
            sign = 1
        n=sign*n # convert n to absolute
        xp = 1

        while n > 0:
            last_bit = n&1

            if last_bit:
                xp = xp * x
            x = x*x
            # print(n, last_bit, xp, x)

            # right shift
            n = n >> 1
        # use sign information to return value
        if sign == 1:
            return xp
        if sign == -1:
            return 1/xp

    def myPow2(self, x: float, n: int) -> float:
        """
        naive power immplementation
        complexity: O(n)
        """
        if n < 0:
            sign = -1
        else:
            sign = 1
        n=sign*n # convert n to absolute
        xp = 1
        for i in range(n):
            xp = xp*x

        # use sign information to return value
        if sign == 1:
            return xp
        if sign == -1:
            return 1/xp

q = Solution()
print(q.myPow(3, -3))
print(q.myPow2(3, -3))