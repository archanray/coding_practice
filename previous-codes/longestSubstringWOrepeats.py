class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        longest substring without repeating characters
        sliding window + some variables for tracking
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        best_string = s[0]
        l = 0
        for i in range(1,len(s)):
            # print(s[i])
            if s[i] in s[l:i]:
                # print("in if loop:", s[i], s[l:i])
                index_of_clash = s[l:i].index(s[i])
                l=l+index_of_clash+1
            else:
                current_string = s[l:i+1]
                # print("in else loop:", current_string, best_string)
                if len(current_string) >= len(best_string):
                    best_string = current_string
                # print("after swapping:", best_string)
        return len(best_string)#, best_string
q = Solution()
print(q.lengthOfLongestSubstring("bbtablud"))