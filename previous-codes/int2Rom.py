class Solution:
    def numToRoman(self, num:int, pos:int, length:int) -> str:
        # convert single digit num to roman string
        if pos == length-1:
            # number is single digit
            if num == 0:
                return ""
            if num > 0 and num < 4:
                return "I"*num
            if num == 4:
                return "IV"
            if num == 5:
                return "V"
            if num > 5 and num < 9:
                return "V"+"I"*(num-5)
            if num == 9:
                return "IX"
        if pos < length-1:
            pass
        return strNum

    def inToRoman(self, num:int) -> str:
        # convert int to str
        num = str(num)
        # start traversing the number in reverse
        n = len(num)
        result = ""
        for i in range(n-1,-1,-1):
            # convert digit to roman
            roman = self.numToRoman(int(num[i]), i, n)
            # add to the result
            result = roman + result
        return result
