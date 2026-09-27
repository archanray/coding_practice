# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
class Solution:
    def isAlienSorted(self, words, order):
        # list dict as character, index in the given order
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            # check if consecutive words are in order, if yes, then the whole list is in order
            word1 = words[i]
            word2 = words[i+1]
            flag = True
            # only run for the smallest length of the words
            for j in range(min(len(word1), len(word2))):
                # if the characters don't match
                if word1[j] != word2[j]:
                    # check if their orders are the correct
                    if order_index[word1[j]] > order_index[word2[j]]:
                        # if not, return false
                        return False
                    # if the first different character is found, break the loop
                    flag = False
                    break
            # if the for loop ran correctly then the following runs
            if flag:
                # if the first word is greater than the second word, return false
                if len(word1) > len(word2):
                    return False
        return True
# Time complexity: O(C), where C is the total content of words.
# Space complexity: O(1).
# Test case:
# ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# ["kuvp","q"], order = "ngxlkthsjuoqcpavbfdermiywz"
# ["hello","hello"], order = "abcdefghijklmnopqrstuvwxyz"
input = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(input, order))