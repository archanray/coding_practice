class Solution():
    def findAnagrams(self, inputStr, target):
        # code to find all anagrams in a string
        output = []
        m, n = len(inputStr), len(target)
        if m < n:
            return output

        freq_target = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(n):
            window[ord(inputStr[i])-ord("a")] += 1
            freq_target[ord(target[i])-ord("a")] += 1

        if freq_target == window:
            output.append(0)

        for i in range(n,m):
            window[ord(inputStr[i-n]) - ord("a")] -= 1
            window[ord(inputStr[i]) - ord("a")] += 1
            if window == freq_target:
                output.append(i-n+1)
        return output

txt = "cbaebabacd"
pat = "abc"
q = Solution()
print(q.findAnagrams(txt, pat))