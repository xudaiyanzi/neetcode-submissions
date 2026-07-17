class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        if s[0] == ')' or s[-1] == '(':
            return False

        for char in s:
            if hi < 0:
                return False
            if char == '(':
                lo += 1
                hi += 1
            elif char == ')':
                lo = max(lo - 1, 0)
                hi -= 1
            else:
                lo = max(lo - 1, 0)
                hi += 1
        
        return lo == 0 and hi >= 0