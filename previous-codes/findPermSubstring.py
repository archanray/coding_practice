from collections import Counter
class Solution:
    def checkDicts(self, D1, D2):
        for key in D2.keys():
            if key in D1:
                if D2[key] == D1[key]:
                    pass
                else:
                    return False
            else:
                return False
        return True
    def findSubstring(self, s1, s2):
        """
        s1 is the main string
        s2 is the pattern
        """
        # create a hashmap
        dictQuery = Counter(s2)
        windowSize = len(s2)

        for i in range(len(s1)):
            if i > len(s1) - len(s2):
                return False
            currentString = s1[i:i+windowSize]
            dictParent = Counter (currentString)
            flag = self.checkDicts(dictQuery, dictParent)
            if flag:
                return True
        return False

s1 = "afggeh"
s2 = "he"
q = Solution()
print(q.findSubstring(s1, s2))