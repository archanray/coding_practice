class Solution:
    def rootedSearch(self, word, midpoint):
        print(word, midpoint)
        count = 0
        j = midpoint+1
        for i in range(midpoint+1):
            if word[i] == word[j].lower():
                j += 1
                count += 1
            else:
                count = 0
                j = midpoint+1
        return count
            
    def pattern(self, word):
        n = len(word)
        l1, r1, l2, r2 = 0, 0, 0, 0
        count = 0
        while r1 < n-1 and r2 < n-1:
            # gran the indices of the lowercase string
            while word[r1].islower():
                r1+= 1
            if r1>l1:
                r1 -= 1
            print("first while:", l1, r1, l2, r2, count)
            l2, r2 = r1+1, r1+1
            while r2 < n and word[r2].isupper() and l2 > 0:
                r2 += 1
                print("second while:", l1, r1, l2, r2)
            if r2 > l2:
                r2 -= 1
            # 0->5, 6->8 => 3->5, 6->8
            l1 = r1-(r2-l2)
            print("before word search:", l1, r1, l2, r2)
            if r1 >= l1 and l1>=0:
                count += self.rootedSearch(word[l1:r2+1], r1-l1)
            l1, r1, l2, r2 = r2+1, r2+1, r2+1, r2+1
        return count
    
print(Solution().pattern("ABCabcAefG"))