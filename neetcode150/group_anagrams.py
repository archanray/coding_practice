from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Solutions --
        1) Sort each string and then check for match. O(m*n log n)
        2) Hashtable
        """
        string_dict = defaultdict(list)
        for s in strs:
            string_dict["".join(sorted(s))].append(s)
        groupList = []
        for k in string_dict.keys():
            groupList.append(string_dict[k])
        return groupList

q = Solution()
print(q.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))