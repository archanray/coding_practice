# LC: hard
from collections import Counter
# code to find the smallest window in a string containing all characters of another string
class Solution:
    def minWindow(self, s, t):
        # complexity: O(n)
        # check if either s or t is empty
        if not s or not t:
            return ""
        # create a dictionary to store the count of each character in t
        dict_t = Counter(t)
        # store the length of the dictionary
        required = len(dict_t)
        # initialize the left and right pointers
        l, r = 0, 0
        # formed keeps track of the number of characters in t which have been matched
        formed = 0
        # create a dictionary to store the count of each character in the window
        window_counts = {}
        # store the length of the string
        ans = float("inf"), None, None
        # loop through the main string
        while r < len(s):
            # get the character at the right pointer
            character = s[r]
            # add the character to the window dictionary
            window_counts[character] = window_counts.get(character, 0) + 1
            # check if the character is in the query dictionary and the count of 
            # the character in the window is equal to the count of the character in the query 
            # dictionary
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # loop through the main string, initiates if the window has been formed
            while l <= r and formed == required:
                # get the character at the left pointer
                character = s[l]
                # check if the current window is the smallest
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # remove the character from the window dictionary
                window_counts[character] -= 1
                # check if the character is in the query dictionary and the count of
                # the character in the window is less than the count of the character in the query
                # dictionary
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                # move the left pointer
                l += 1
            # move the right pointer
            r += 1
        # return the smallest window
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

q = Solution()
print(q.smallestWindow("ADOBECODEBANC", "ABC")) # "BANC"