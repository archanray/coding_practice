# Return an array of all the palindrome pairs of words.
# You must write an algorithm with O(sum of words[i].length) runtime complexity.
class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]
        word_lookup = {word: i for i, word in enumerate(words)}
        ans = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in word_lookup and word_lookup[back] != i:
                        #ans.append([word_lookup[back], i])
                        ans.append(words[word_lookup[back]]+words[i])
                if j != len(word) and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back in word_lookup and word_lookup[back] != i:
                        ans.append(words[i]+words[word_lookup[back]])
                        #ans.append([i, word_lookup[back]])
        return ans
s = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(s.palindromePairs(words)) # [[1,0],[0,1],[3,2],[2,4]]