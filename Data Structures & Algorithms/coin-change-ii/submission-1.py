class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        n = len(coins)

        def dfs(i, remain):
            if remain < 0 or i >= n:
                return 0 
            if remain == 0:
                return 1
            if (i, remain) in dp:
                return dp[(i, remain)]
            use = dfs(i, remain - coins[i])
            skip = dfs( i + 1, remain)
            dp[(i, remain)] = use + skip
            return dp[(i, remain)]
        
        return dfs(0, amount)