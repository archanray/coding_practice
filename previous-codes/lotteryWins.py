class Solution():
    def lottery(self, coupons):
        """
        Several coupons are placed in a row, and to win the 
        prize you need to pick at least 2 coupons of the 
        same value. You can only pick consecutive coupons 
        from the row. Each coupon costs 1 coin, find the minimum 
        number of coins needed to obtain the prize or, -1 if it's 
        not possible.
        
        Input: coupons = [5, 3, 4, 2, 3, 4, 5, 7]
        Output: 4
        Explanation:
        Because you can buy coupons with values 
        [3, 4, 2, 3] or [4, 2, 3, 4]

        Input: coupons = [3, 6, 1, 9]
        Output: -1
        """
        l = 0
        length = float("inf")
        for i in range(1,len(coupons)):
            v = coupons[i]
            if v in coupons[l:i]:
                match_index = coupons[l:i].index(v)
                local_len = i-match_index+1
                length = min(length, local_len)
                l = match_index+1
        if length == float("inf"):
            length = -1
        return length

q = Solution()
print(q.lottery([3, 6, 1, 9]))