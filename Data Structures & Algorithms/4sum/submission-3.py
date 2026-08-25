class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        if n < 4:
            return res
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                val = target - nums[i] - nums[j]

                l, r = j + 1, n - 1

                while l < r:
                    curr = nums[l] + nums[r]
                    if curr > val:
                        r -= 1
                    elif curr < val:
                        l += 1
                    else:
                        candidate = [nums[i], nums[j], nums[l], nums[r]]
                        l += 1
                        r -= 1
                        if res and res[-1] == candidate:
                            continue
                        res.append(candidate)

        return res