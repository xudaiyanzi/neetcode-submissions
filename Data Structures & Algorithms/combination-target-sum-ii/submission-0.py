class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def backtrack(i, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return
            
            for new in range(i, n):
                if new > i and candidates[new] == candidates[new - 1]:
                    continue
                path.append(candidates[new])
                backtrack(new + 1, path, total + candidates[new])
                path.pop()

        backtrack(0, [], 0)
        return res