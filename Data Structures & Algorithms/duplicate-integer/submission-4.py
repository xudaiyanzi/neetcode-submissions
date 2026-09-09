class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0 or n == 1:
            return False

        nums.sort()
        slow, fast = 0, 1

        while fast < n:
            if nums[slow] != nums[fast]:
                slow += 1
            else:
                return True
            fast += 1

        return False
