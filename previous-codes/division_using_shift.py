class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0 and divisor > 0:
            sign = -1
        elif dividend > 0 and divisor < 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        neg_lim = -(2**31)
        pos_lim = 2**31-1
        result = min(max(neg_lim, result), pos_lim)
        return result