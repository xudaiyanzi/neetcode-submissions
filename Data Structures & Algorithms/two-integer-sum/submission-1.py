class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []
        
        n_dic = {}

        for i in range(len(nums)):
            if nums[i] in n_dic:
                return [n_dic[nums[i]], i]

            n_dic[target - nums[i]] = i
        return []