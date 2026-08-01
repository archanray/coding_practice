class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        smallest tracker tracks the smallest price
        profit tracks the max profit
        """
        if not prices:
            return 0
        smallest_tracker = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= smallest_tracker:
                smallest_tracker = prices[i]
            profit = max(profit, prices[i]-smallest_tracker)
        return profit