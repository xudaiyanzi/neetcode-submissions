class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]
            l, r = i + 1, n - 1
            
            while l < r:
                curr = nums[l] + nums[r]
                if curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    candidate = [nums[i], nums[l], nums[r]]
                    l += 1
                    r -= 1
                    if res and res[-1] == candidate:
                        continue
                    res.append(candidate)
        
        return res