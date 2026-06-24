class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i, isBuying):
            if i >= n:
                return 0
            
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]
            
            cool = dfs(i + 1, isBuying)
            if isBuying:
                buy = dfs(i + 1, not isBuying) - prices[i]
                dp[(i, isBuying)] = max(buy, cool)
            else:
                sell = dfs(i + 2, not isBuying) + prices[i]
                dp[(i, isBuying)] = max(sell, cool)
            
            return dp[(i, isBuying)]

        return dfs(0, True)


