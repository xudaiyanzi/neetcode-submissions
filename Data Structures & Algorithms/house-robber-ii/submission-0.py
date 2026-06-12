class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)
        
        def rob_liner(houses):
            h_n = len(houses)
            dp = [0] * h_n
            dp[0], dp[1] = houses[0], max(houses[0], houses[1])

            for i in range(2, h_n):
                dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])

            return dp[h_n - 1]
        
        return max(rob_liner(nums[:-1]), rob_liner(nums[1:]))