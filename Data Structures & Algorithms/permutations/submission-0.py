class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(path, used):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(0, n):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                used[i] = False
                path.pop()
        
        backtrack([], used)
        return res