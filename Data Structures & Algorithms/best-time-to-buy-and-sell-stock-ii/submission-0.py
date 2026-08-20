class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        res = [0] * n
        lowest = prices[0]

        for i in range(1, n):

            if lowest < prices[i]:
                res[i] = res[i - 1] + prices[i] - lowest
            else:
                res[i] = res[i - 1]
            lowest = prices[i]
        
        return res[-1]