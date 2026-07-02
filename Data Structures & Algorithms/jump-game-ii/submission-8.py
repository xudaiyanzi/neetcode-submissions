class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        curr, farthest = 0, 0
        count = 0

        for i in range(n - 1):
            farthest = max(nums[i] + i, farthest)

            if i == curr:
                count += 1
                curr = farthest
        
        return count
                
        
            
