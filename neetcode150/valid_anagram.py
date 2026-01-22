class Solution:
    def isAnagramSorting(self, s:str, t:str) -> bool:
        """
        Time complexity: O(nlog n), space complexity O(n)
        """
        if not (len(s) == len(t)):
            return False
        s = [ord(char) for char in s]
        s.sort()
        t = [ord(char) for char in t]
        t.sort()
        if s == t:
            return True
        return False
    
    def isAnagramSorted(self, s:str, t:str) -> bool:
        """
        Time complexity: O(nlog n)
        """
        if not (len(s) == len(t)):
            return False
        return sorted(s) == sorted(t)
    
    def isAnagram(self, s:str, t:str) -> bool:
        """
        using hashmap, time complexity O(n+m), space complexity is O(1) since fixed.
        """
        if not (len(s) == len(t)):
            return False
        s_set = {}
        t_set = {}
        for i in range(len(s)):
            s_set[s[i]] = 1+ s_set.get(s[i], 0)
            t_set[t[i]] = 1+ t_set.get(t[i], 0)
        return s_set == t_set
    
q = Solution()
print(q.isAnagram(s = "racecar", t = "carrace"))