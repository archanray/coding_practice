class Solution:
    def minDistanceSlow(self, word1:str, word2:str) -> int:
        """
        slow recursion
        """
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        elif word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            return 1+min(self.minDistance(word1[1:], word2),\
                         self.minDistance(word1, word2[1:]),\
                         self.minDistance(word1[1:], word2[1:]))

    def minDistanceFast(self, word1:str, word2:str) -> int:
        n = len(word1)
        m = len(word2)
        d = []
        for i in range(n+1):
            rows = [0 for j in range(m+1)]
            d.append(rows)
        for i in range(1,n+1):
            d[i][0] = i
        for j in range(1,m+1):
            d[0][j] = j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j] + 1,\
                                  d[i][j-1] + 1,\
                                  d[i-1][j-1]+1)
        return d[n][m]



q = Solution()
input1 = "abba" #"intention"
input2 = "abba" #"execution"
print(q.minDistanceFast(input1, input2))