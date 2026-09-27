import numpy as np
import string

def go_back_and_find(s: list, start2: int, start1: int):
    hash2 = []
    length2 = 0
    for i in range(start2, start1-1, -1):
        if s[i] not in hash2:
            hash2.append(s[i])
            length2 += 1
        else:
            break
    start2 = i+1
    return start2, length2, hash2
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        length1 = 0
        length2 = 0
        start1 = 0
        start2 = 0
        hash1 = []
        hash2 = []
        s = list(s)
        for i in range(len(s)):
            if s[i] not in hash2:
                hash2.append(s[i])
                length2 += 1
                if length1 <= length2:
                    hash1 = hash2
                    length1 = length2
                    start1 = start2
            else:
                start2, length2, hash2 = go_back_and_find(s, i, start1)
            # print(length1, length2, start1, start2)
            pass
        return length1

