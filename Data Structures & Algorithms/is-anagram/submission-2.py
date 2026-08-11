class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        
        dic_s = {}

        for char in s:
            dic_s[char] = dic_s.get(char, 0) + 1
        
        for char in t:
            if char not in dic_s:
                return False

            dic_s[char] -= 1

            if dic_s[char] == 0:
                del dic_s[char]
        
        if not dic_s:
            return True
        else:
            return False

        