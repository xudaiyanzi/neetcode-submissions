class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)
        
        def rob_liner(houses):
            h_n = len(houses)
            pre2, pre1 = houses[0], max(houses[0], houses[1])

            for i in range(2, h_n):
                curr = max(pre2 + houses[i], pre1)
                pre2 = pre1
                pre1 = curr

            return pre1
        
        return max(rob_liner(nums[:-1]), rob_liner(nums[1:]))