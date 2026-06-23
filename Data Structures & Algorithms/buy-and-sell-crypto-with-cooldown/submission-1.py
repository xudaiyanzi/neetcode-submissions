class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i, isBuy):
            if i >= n:
                return 0
            if (i, isBuy) in dp:
                return dp[(i, isBuy)]

            cool = dfs(i + 1, isBuy)
            if isBuy:
                buy = dfs(i + 1, not isBuy) - prices[i]
                dp[(i, isBuy)] = max(buy, cool)
            else:
                sell = dfs(i + 2, not isBuy) + prices[i]
                dp[(i, isBuy)] = max(sell, cool)
            return dp[(i, isBuy)]
        
        return dfs(0, True)


