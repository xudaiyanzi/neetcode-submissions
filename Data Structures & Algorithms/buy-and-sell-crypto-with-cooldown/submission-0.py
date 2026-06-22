class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold_prev = float('-inf')
        sold_prev = 0
        free_prev = 0

        for price in prices:
            hold = max(hold_prev, free_prev - price)
            sold = hold_prev + price
            free = max(free_prev, sold_prev)
            hold_prev, sold_prev, free_prev = hold, sold, free

        return max(free_prev, sold_prev)