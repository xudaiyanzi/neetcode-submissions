from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        for key, value in dic.items():
            n = len(value)
            if n >= 2:

                l, r = 0, n - 1
                while  l < r:
                    curr = value[r] - value[l]
                    if curr > k:
                        l += 1
                    else:
                        return True
                
        
        return False