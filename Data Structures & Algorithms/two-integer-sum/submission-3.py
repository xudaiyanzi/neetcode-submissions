class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in record:
                return [record[nums[i]], i]
            record[target - nums[i]] = i
        
        return [-1, -1]