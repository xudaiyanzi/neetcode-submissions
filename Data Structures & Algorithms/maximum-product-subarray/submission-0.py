class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1

        for i in range(len(nums)):
            new_max = max(nums[i], nums[i] * cur_max, nums[i] * cur_min)
            new_min = min(nums[i], nums[i] * cur_max, nums[i] * cur_min)
            cur_max, cur_min = new_max, new_min
            res = max(res, cur_max)
        
        return res
        

            