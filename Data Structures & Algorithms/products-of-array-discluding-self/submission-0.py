class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_p = nums[0]
        post_p = 1
        n = len(nums)
        pre_p_list = [1]
        res = [1] * n

        for i in range(1, n):
            pre_p_list.append(pre_p)
            pre_p *= nums[i]
        
        for j in range(n - 1, -1, -1):
            res[j] = pre_p_list[j] * post_p
            post_p *= nums[j]

        return res

            