class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 0:
            return False
        
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            else:
                num_set.add(n)
        return False