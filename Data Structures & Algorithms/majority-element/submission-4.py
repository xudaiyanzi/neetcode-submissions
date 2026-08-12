class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        same, same_count = 0, 0

        for n in nums:

            if same_count > len(nums) // 2:
                return same

            if n == same:
                same_count += 1
            else:
                if same_count > 0:
                    same_count -= 1
                if same_count == 0:
                    same = n
                    same_count += 1

        return same