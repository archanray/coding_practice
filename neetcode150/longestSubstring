class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        if s[i] is in seen_hash, then we have a duplicate, and we need to update the start_id to be the max of the current start_id and the index of the last occurrence of s[i]+1
        we also need to update the seen_hash with the current index of s[i]
        we also need to update the max_length with the current length of the substring, which is i - start_id + 1
        """
        if len(s) < 2:
            return len(s)
        max_length = 0
        start_id = 0
        seen_hash = {}
        for i in range(len(s)):
            if s[i] in seen_hash.keys():
                start_id = max(start_id, seen_hash[s[i]]+1)
            seen_hash[s[i]] = i
            max_length = max(max_length, i - start_id+1)
        return max(max_length, i - start_id)
    
q = Solution()
print(q.lengthOfLongestSubstring("au"), q.lengthOfLongestSubstring("dvdf"))