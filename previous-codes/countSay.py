class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        medout = self.countAndSay(n-1)
        count = 0
        res = ""
        for i in range(len(medout)):
            count += 1
            if i>0 and medout[i] != medout[i-1]:
                res = res + str(count-1) + str(medout[i-1])
                count = 1
            
        res = res+str(count) + str(medout[i])
        return res

q = Solution()

print(q.countAndSay(5))



