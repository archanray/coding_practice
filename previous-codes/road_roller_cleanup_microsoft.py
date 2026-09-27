class Solution:
    def solution(self, X, Y, width):
        count = 1
        X = sorted(X)
        start = X[0]
        for i in range(1,len(X)):
            if X[i] <= start + width:
                continue
            else:
                start = X[i]
                count += 1
        return count
    
X = [0,3,6,5]
Y = [0,3,2,4]
width = 1
print(Solution().solution(X, Y, width))