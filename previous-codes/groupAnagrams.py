class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        code to group anagrams together
        """
        dict_ = {}
        for string in strs:
            string_key = "".join(sorted(string))
            if string_key not in dict_:
                dict_[string_key] = [string]
            else:
                dict_[string_key].append(string)
        return_list = []
        for key in dict_.keys():
            l_new = dict_[key]
            return_list.append(l_new)
        return return_list
q = Solution()
print(q.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))