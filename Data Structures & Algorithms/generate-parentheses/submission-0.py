class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, count_start, count_end):
            if len(path) == n * 2:
                res.append(''.join(path))
                return
            
            if count_start < n:
                path.append('(')
                backtrack(path, count_start + 1, count_end)
                path.pop()
            
            if count_end < count_start:
                path.append(')')
                backtrack(path, count_start, count_end + 1)
                path.pop()
            
        backtrack([], 0, 0)
        return res
                