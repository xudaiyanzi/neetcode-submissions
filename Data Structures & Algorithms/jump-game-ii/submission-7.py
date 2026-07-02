class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(n):
            for j in range(0, i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[j] + 1, dp[i])
        
        return dp[n - 1]
        
        
            
