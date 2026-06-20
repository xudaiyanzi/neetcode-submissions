class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total / 2
        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return True
            
            if i == len(nums):
                return False
            
            return dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)
        
        return dfs(0, target)
        
