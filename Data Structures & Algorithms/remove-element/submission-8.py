class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p1, p2 = 0, n - 1

        while p1 <= p2:
            if nums[p1] == val:
                while p2 >= 0 and nums[p2] == val:
                    p2 -= 1
                
                if p1 < p2:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p2 -= 1
            p1 += 1
        
        return p2 + 1
            