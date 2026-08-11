class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n not in num_set:
                num_set.add(n)
            
            else:
                return True
            
        return False