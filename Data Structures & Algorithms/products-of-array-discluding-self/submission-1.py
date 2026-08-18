class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        post = [1] * n
        for j in range(n - 2, -1, -1):
            post[j] = post[j + 1] * nums[j + 1]
        
        res = [1] * n

        for i in range(0, n):
            res[i] = pre[i] * post[i]
        
        return res