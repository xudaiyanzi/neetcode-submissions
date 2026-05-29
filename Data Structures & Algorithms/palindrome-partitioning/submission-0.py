class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        def isP(start, end):
            left, right = start, end
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if isP(start, end - 1):
                    path.append(s[start : end])
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
            
