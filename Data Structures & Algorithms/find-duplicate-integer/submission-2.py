class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = len(nums)
        if m <= 1:
            return -1
        n = m - 1

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        meet = slow

        slow = 0
        while True:
            slow = nums[slow]
            meet = nums[meet]
            if slow == meet:
                return slow
        
