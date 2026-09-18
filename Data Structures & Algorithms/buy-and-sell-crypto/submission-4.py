class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        most = prices[0]
        res = 0
        for i in range(len(prices)):
            if prices[i] < least:
                least = prices[i]
                most = 0
            elif prices[i] > most and res < prices[i]-least:
                most = prices[i]
                res = most-least
        if res > 0:
            return res
        return 0
            
