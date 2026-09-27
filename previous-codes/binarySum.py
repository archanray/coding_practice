# add two binary numbers without converting to ints
class Solution():
    def binSum(self, str1, str2):
        if str1 == "0" and str2 == "0":
            return "0"
        if str1 == "0":
            return str2
        if str2 == "0":
            return str1
        a = str1[::-1]
        b = str2[::-1]
        carry = 0
        res = []
        i, j = 0, 0
        while i < len(a) or j < len(b):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[j]) if j < len(b) else 0
            s = x + y + carry
            carry = s // 2
            res.append(str(s % 2))
            i += 1
            j += 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
    
# test cases
input1 = "11"
input2 = "1"
q = Solution()
print(q.binSum(input1, input2)) # output: 100