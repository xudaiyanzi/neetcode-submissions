class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for n in nums:
            if n - 1 not in num_set:
                count = 1
                while n + 1 in num_set:
                    count += 1
                    n = n + 1
                max_count = max(count, max_count)
        
        return max_count