class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        seen = {0: 1}
        count = 0

        for n in nums:
            curr += n

            count += seen.get(curr - k, 0)

            seen[curr] = seen.get(curr, 0) + 1
        
        return count