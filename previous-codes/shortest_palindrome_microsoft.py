class Solution:
    def shortestPalindrome(self,s):
        n = len(s)
        # find the longest substring which is a palindrome starting at index 0
        dp = [0]*n
        # reverse s and store in t
        t = s[::-1]
        # this O(n^2)
        for i in range(n):
            # the following check is O(n)
            if s[0:i+1] == t[n-1-i:n]:
                dp[i] = i+1
        max_val = 1
        max_index = 0
        for i in range(1,n):
            if dp[i] > max_val:
                max_val = dp[i]
                max_index = i
        # flip the rest and add to the input.
        adder = s[max_index+1:]
        adder = adder[::-1]    
        return adder+s

# input = "abcd"
input = "aacecaaa"
print(Solution().shortestPalindrome(input))