class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        i = 0
        j = i + 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j = i + 1
            else:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
        return max_profit
