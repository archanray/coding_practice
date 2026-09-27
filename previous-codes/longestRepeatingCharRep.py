class Solution:
    def characterReplacement(self, s, k):
        """
        Problem 424: 
        You are given a string 's' and an integer 'k'. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get after performing the above operations.
        """
        char_count = {}
        max_length = 0
        max_count = 0
        window_start = 0
        for window_end in range(len(s)):
            # incrememnt count of current char
            char_count[s[window_end]] = 1 + char_count.get(s[window_end],0)
            # update max count seen so far
            max_count = max(max_count, char_count[s[window_end]])
            
            # shrink window if required
            if window_end - window_start + 1 > max_count + k:
                char_count[s[window_start]] -= 1
                window_start += 1
            
            # update max length of substring with rep chars
            max_length = max(max_length, window_end-window_start+1)
        return max_length