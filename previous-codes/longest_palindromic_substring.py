import numpy as np
import string 

# length of longest palindromic substring
# Time complexity: O(n^2)
# Space complexity: O(1)
# Test case:
# "babad"
# "cbbd"
# "a"
# "ac"
# "trinitrophenylmethylnitramine"
# "trinityeeree"
# "aacabdkacaa"
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2
        return s[start:end + 1]
    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1
    
print(Solution().longestPalindrome("trinityeeree"))

# longest palindromic subsequence
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
print(Solution().longestPalindromeSubseq("trinityeeree"))

# def searchAround(s, i):
#     length = 0
#     palindrome = ""
#     flag = 0
#     if i == 0 or i == len(s)-1:
#         length = 1
#         palindrome = s[int(i)]
#         return length, palindrome, flag
#     for j in np.arange(0,i+0.5,0.5):
#         base = int(np.ceil(i-j))
#         top = int(np.floor(i+j))
#         # print(base, top)
#         if s[base] == s[top]:
#             palindrome = s[base:top+1]
#             length = len(palindrome)
#         else:
#             break
#         if top == len(s)-1:
#             flag = 1
#             break
#     return length, palindrome, flag

# # LoLS:: length of longest subsequence O(1) space requirement
# def centerLoLS(s):
#     strLen = 0
#     reqPal = ""
#     flag = 0
#     for i in np.arange(0,len(s)-0.5, 0.5):
#         # print(s, i)
#         length, maxpal, flag = searchAround(s,i)
#         # print("algo output:", length, maxpal)
#         if length >= strLen:
#             # print("HERE", length, maxpal)
#             strLen = length
#             reqPal = maxpal
#         if flag:
#             return strLen, reqPal        
#         # print("==========================================")
#     return strLen, reqPal

# # print(centerLoLS("babad"))
# # print(centerLoLS("aab"))
# # print(centerLoLS("trinitrophenylmethylnitramine"))
# print(centerLoLS("trinityeeree"))
# # print(centerLoLS("aacabdkacaa"))
# # print(centerLoLS("hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
# # print(centerLoLS("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))
