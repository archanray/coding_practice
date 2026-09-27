class Solution:
    def reverseWords(self, s: str) -> str:
        """
        reverse words
        remove extra spaces
        """
        words = s.split(" ")
        t = ""
        for i in range(len(words)-1, -1, -1):
            if words[i] == "":
                continue
            if words[i] == " ":
                continue
            t += words[i]+" "
        if t[-1] == " ":
            t = t[:-1]
        return t

q = Solution()
print(q.reverseWords("the"))