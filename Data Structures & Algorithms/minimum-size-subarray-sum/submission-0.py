class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        l, n = 0, len(nums)
        res = float('inf')
        for r in range(n):
            curr += nums[r]

            while l <= r and curr >= target:
                res = min(r - l + 1, res)
                curr -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0