class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        
        if not s or not t or len(s) != len(t):
            return False
        
        dic_s = {}

        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1
        
        for j in t:
            if j not in dic_s or dic_s[j] == 0:
                return False
            dic_s[j] -= 1
        return True