class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        sum_list = [0] * n
        sum_list[0] = nums[0]

        for i in range(1, n):
            sum_list[i] = max(nums[i], sum_list[i - 1] + nums[i])
        
        return max(sum_list)