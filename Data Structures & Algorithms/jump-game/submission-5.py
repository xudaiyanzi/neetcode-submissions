class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = nums[0]

        for i in range(1, n):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n - 1:
                return True
        
        return True