class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for price in prices:
            if max_profit < price - min_buy: max_profit = price - min_buy
            if price < min_buy: min_buy=price
        return max_profit
