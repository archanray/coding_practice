# import numpy as np

class Solution:
    def reverse(self, x: int) -> int:
        checkNeg = x < 0
        newX = 0
        if checkNeg:
            x = -x
        while int(x/10)>0:
            stray = x%10
            x = int(x/10)
            newX = 10*newX+stray
        newX = 10*newX+x
        if checkNeg:
            newX = -newX
        # try:
        #     newX = np.int32(newX)
        # except:
        #     newX=0
        if newX < -2**31 or newX > 2**31-1:
            newX=0
        return newX

L = [123, -123, 120, 1534236469]
# L = [123]
for i in range(len(L)):
    sols = Solution()
    print(sols.reverse(L[i]))