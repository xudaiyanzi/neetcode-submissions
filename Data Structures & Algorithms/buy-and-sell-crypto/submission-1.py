class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_indx = 0

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[low_indx]:
                low_indx = i
                
            else:
                profit = prices[i] - prices[low_indx]
                max_profit = max(max_profit, profit)
        
        return max_profit
