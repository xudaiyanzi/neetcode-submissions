class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v1, v2 = None, None
        count1, count2 = 0, 0
        res = []

        for num in nums:
            if num == v1:
                count1 += 1
            elif num == v2:
                count2 += 1
            elif count1 == 0:
                v1 = num
                count1 = 1
            elif count2 == 0:
                v2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        n = len(nums)
        for c in (v1, v2):
            if c is not None and nums.count(c) > n // 3:
                res.append(c)
        return res
            