class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def dfs(i, remain):
            if (i, remain) in dp:
                return dp[(i, remain)]
            if i == n:
                if remain == 0:
                    return 1
                else:
                    return 0
            elif i < n:
                pos = dfs(i + 1, remain - nums[i])
                neg = dfs(i + 1, remain + nums[i])
                count = pos + neg
                dp[(i, remain)] = count
            return count
        
        return dfs(0, target)
        