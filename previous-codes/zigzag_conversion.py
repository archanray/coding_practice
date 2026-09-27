class Solution:
    def convert(self, s:str, numRows:int) -> str:
        if numRows == 1:
            return s
        lengthS = len(s)
        rearranged_letters = []
        principal_centers = []
        for index in range(numRows):
            centers = list(range(index, lengthS, numRows-1+numRows-2+1))
            if index == 0:
                principal_centers = centers
            if index > 0 and index != numRows-1:
                off_centers = [principal_centers[x]+numRows-1+numRows-2+1-index\
                                for x in range(0, len(principal_centers))\
                                if principal_centers[x]+numRows-1+numRows-2+1-index < lengthS]
                all_centers = [None]*(len(centers)+len(off_centers))
                all_centers[::2] = centers
                all_centers[1::2] = off_centers
                centers = all_centers
            q = [s[x] for x in centers]
            # print(q)
            rearranged_letters += q
        return ''.join(rearranged_letters)


L = ["conversion", "PAYPALISHIRING", "A", "ABCD"]
# L = ["ABCD"]
rows = [4,3,1,3]
# rows = [3]
for i in range(len(L)):
    sols = Solution()
    print(sols.convert(L[i], rows[i]))