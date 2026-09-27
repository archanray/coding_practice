class Solution():
    def grayCode(self, n):
        out = [0] # starting with 0
        for i in range(n):
            for j in range(len(out)-1, -1, -1):
                # for all numbers in the list
                # do bitwise OR with the current bit
                out.append(out[j] | (1<<i))
        return out


q = Solution()
print(q.grayCode(4))