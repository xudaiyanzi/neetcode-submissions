class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, n - 1

            while l < r:
                val = nums[l] + nums[r]
                if val > 0 - nums[i]:
                    r -= 1
                elif val < 0 - nums[i]:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res