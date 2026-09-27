class Solution():
    def int2str(self, strnum):
        """
        convert string to number
        """
        dict_num = {0:"0",1:"1",2:"2",3:"3",4:"4",\
                    5:"5",6:"6",7:"7",8:"8",9:"9"}
        numstr = ""
        count = 0
        while strnum > 0:
            count += 1
            r = strnum % 10
            numstr = dict_num[r] + numstr
            strnum = strnum//10
        if count == 0:
            return "0"
        return numstr
        
    def str2int(self, num):
        """
        convert a str number to integer without using int
        """
        dict_num = {"0":0,"1":1,"2":2,"3":3,"4":4,\
                    "5":5,"6":6,"7":7,"8":8,"9":9}
        r = 0
        n = len(num)
        for i in range(n-1,-1,-1):
            r += (10**(n-i-1))*dict_num[num[i]]
        return r

    def multiply(self, num1: str, num2: str) -> str:
        """
        """
        num1 = self.str2int(num1)
        num2 = self.str2int(num2)
        mult = num1*num2

        return self.int2str(mult)

q = Solution()
print(q.multiply("123", "456"))
print(q.multiply("0", "1"))