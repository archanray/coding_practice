class Solution:
    def find_max(self, list1, list2) -> int:
        if len(list1) == 1:
            return list1[0]
        cost = 0
        n = len(list1)
        l1 = list1[0] + self.find_max(list1[1:], list2[1:])
        l2 = self.find_max(list2[1:], list1[1:])
        if l1 > l2:
            cost += l1
        else:
            cost += l2
        return cost

    def TSP(self, list1, list2) -> int:
        # recursive and expensive!
        return max(self.find_max(list1, list2), self.find_max(list2, list1))
    
    def TSP_DP(self, A, B, cost) -> int:
        # dynamic programming solution for TSP problem
        # dp[i] = max(dp[i-1], dp[i-1]+list1[i], dp[i-1]+list2[i])
        if len(A) != len(B):
            return "Error: unequal lists"
        n = len(A)
        dp = [[0]*2 for i in range(n)]
        # establish the base cases
        dp[0][0] = A[0]
        dp[0][1] = B[0]
        dp[1][0] = max(A[0]+A[1], B[0])
        dp[1][1] = max(B[0]+B[1], A[0])
        # solve the subsequent problems 
        for i in range(2,n):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1]) + A[i]
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]) + B[i]
        # return value
        return max(dp[n-1][0], dp[n-1][1])

input1 = [23, 4, 5, 20] # [12, 14, 15] # [25, 1, 30, 12, 10] # [23, 4, 5, 20]
input2 = [21, 1, 10, 100] # [15, 1, 3] # [10, 12, 3, 1, 200] # [21, 1, 10, 100]
cost = 0
q = Solution()
print(q.TSP(input1, input2))
print(q.TSP_DP(input1, input2, cost))
