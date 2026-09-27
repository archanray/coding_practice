class Solution:
    def checkValidity(self, time1):
        hours1 = int(time1[0])*10 + int(time1[1])
        minutes1 = int(time1[2])*10 + int(time1[3])
        return 0<=hours1<=24 and 0<=minutes1<=59
    
    def timeDifference(self, time1, time2):
        hours1 = int(time1[0])*10 + int(time1[1])
        minutes1 = int(time1[2])*10 + int(time1[3])
        time1 = hours1 * 60 + minutes1
        
        hours2 = int(time2[0])*10 + int(time2[1])
        minutes2 = int(time2[2])*10 + int(time2[3])
        time2 = hours2 * 60 + minutes2
        
        totalTimeInOneDay = 24*60
        if time2 <= time1:
            return totalTimeInOneDay - time1 + time2
        else:
            return time2-time1
    
    def dfs(self, current):
        # print(current)
        if len(current) > 4:
            return
        if len(current) == 4 and self.checkValidity(current):
            currentTimeDiff = self.timeDifference(self.charsInInput, current)
            if self.minTimeDiff >= currentTimeDiff:
                self.minTimeDiff = currentTimeDiff
                self.res = current
            return
        for i in range(4):
            self.dfs(current + self.charsInInput[i])
        return None
    
    def solution(self, time):
        if len(time) > 5:
            return -1
        self.time  = time
        self.charsInInput = [c for c in time if c!=":"]
        if not self.checkValidity(self.charsInInput):
            return -1
        self.minTimeDiff = self.timeDifference(self.charsInInput, self.charsInInput)
        self.res = self.charsInInput
        self.dfs(self.charsInInput[0])
        # print(self.res, self.minTimeDiff)
        return self.res[:2]+":"+self.res[2:]

input = "19:34"
print(Solution().solution(input))