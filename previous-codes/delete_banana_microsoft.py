class Solution:
    def solution(self, string):
        a, b, n = 0, 0, 0
        for i in range(len(string)):
            if string[i] == "A":
                a += 1
            if string[i] == "B":
                b += 1
            if string[i] == "N":
                n += 1
        return int(min(a/3, b/1, n/2))

# NAABXXAN, QABAAAWOBL, NAANAAXNABABYNNBZ
input = "NAABXXAN"
print(Solution().solution(input))
        
        