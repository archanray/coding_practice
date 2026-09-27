def ranger(num):
    if num > 2**31-1:
        num = 2**31-1
    if num < -2**31:
        num = -2**31
    return num

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        mult = 0
        num = 0
        list_of_ints = [str(x) for x in list(range(10))]
        admissible = ["-", "+"]
        lead_mult = 1
        read = 0

        for i in range(len(s)):
            if s[i] == " " and read == 0:
                read = 1
            elif s[i] == " " and read >= 2:
                read = 4
            if s[i] in admissible and read == 1:
                read = 2
            elif s[i] in admissible and read == 0:
                read = 2
            elif s[i] in admissible and read >= 2:
                read = 4
            # elif s[i] in admissible and read == 3:
            #     read = 4
            if s[i] not in list_of_ints and s[i] not in admissible and s[i] != " ":
                read = 4
            if s[i] in list_of_ints and read < 4:
                read = 3
                if s[i-1] == "-" and i > 0:
                    lead_mult = -1
                num = num*10+int(s[i])

            if read == 4:
                return ranger(num*lead_mult)
            
        return ranger(num*lead_mult)


q = Solution()

print(q.myAtoi("  +  413")) # output should be 0

print(q.myAtoi("words and 987")) # output should be 0

print(q.myAtoi("   -41")) # output should be -41

print(q.myAtoi("+-12")) # output should be 0

print(q.myAtoi("-+12")) # output should be 0

print(q.myAtoi("-41")) # output should be -41

print(q.myAtoi("4193 with words")) # output should be 4193

print(q.myAtoi("00000-42a1234")) # output should be 0

print(q.myAtoi("3.14159")) # output should be 3

print(q.myAtoi("  -0012a42")) # output should be -12

print(q.myAtoi("   +0 123")) # output should be 0

print(q.myAtoi("123-")) # output should be 123
