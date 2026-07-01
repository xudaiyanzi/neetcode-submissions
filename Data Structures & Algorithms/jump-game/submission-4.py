class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for possible_length in range(1, nums[i] + 1):
                new_pos = i + possible_length

                if new_pos < n:
                    dp[new_pos] = True
        
        return dp[n - 1]