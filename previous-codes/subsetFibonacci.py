import numpy as np
class Solution():
    # formula: 5*n^2+4 or 5*n^2-4 is a fibonacci
    def checkSquare(self, num):
        if num <= 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = left+(right-left) // 2
            square = mid**2
            if square == num:
                return True
            elif square <= num:
                left = mid+1
            else:
                right = mid-1
        return False
    def slowCheckSquare(self, num):
        roundSqrtNum = np.round(np.sqrt(num))
        if num == roundSqrtNum**2:
            return True
        else:
            return False
    def checkFibo(self, num):
        if num == 0:
            return False
        nbase = 5*(num**2)
        n1 = nbase+4
        n2 = nbase-4
        if self.checkSquare(n1) or self.checkSquare(n2):
            return True
        # if self.slowCheckSquare(n1) or self.slowCheckSquare(n2):
        #     return True
        else:
            return False
    def findSubset(self, nums):
        outputs = []
        for i in range(len(nums)):
            if self.checkFibo(nums[i]):
                outputs.append(nums[i])
            else:
                pass
        return outputs

arr = [0, 2, 8, 5, 2, 1, 4, 13, 23]
q = Solution()
print(q.findSubset(arr))