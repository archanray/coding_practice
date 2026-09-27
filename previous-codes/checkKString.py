from copy import copy
import numpy as np
class Solution():
    def editDistance(self, string1, string2):
        m = len(string1)
        n = len(string2)
        dp = np.zeros((m+1, n+1)).astype(int)
        dp[0,:] = list(range(m+1))
        dp[:,0] = list(range(n+1))
        
        for i in range(1,m+1):
            for j in range(1, n+1):
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[m,n]
    
    def kPalindromeCheck(self, string, k):
        str1 = string
        str2 = string[-1::-1]
        distance = self.editDistance(str1, str2)
        if distance <= 2*k:
            return True
        return False

intputStr = "acdcb"
K = 1
q = Solution()
print(q.kPalindromeCheck(intputStr, K))