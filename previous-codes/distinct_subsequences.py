# Given two strings s and t, return the number of distinct subsequences of s which equals t.
class Solution:
    def numDistinct(self, s, t):
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)] # len(s)+1 \times len(t)+1 matrix
        for i in range(len(s) + 1):
            dp[i][0] = 1    # set first column to 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # if characters are equal, we can choose to use the character or not
                if s[i-1] == t[j-1]:
                    # if we choose to use the character, we add the number of ways to form the previous substring
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # if characters are not equal, we can only choose not to use the character
                    dp[i][j] = dp[i-1][j]
        # return the number of ways to form the entire substring
        return dp[-1][-1]
# Time complexity: O(mn), where m is the length of s and n is the length of t.
# Space complexity: O(mn).
# Test case:
# "rabbbit", "rabbit"
# "babgbag", "bag"
# "a", "a"
# "a", "b"
# "a", ""
# "a", "a"
input = "rabbbit"
target = "rabbit"
print(Solution().numDistinct(input, target))