class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dic1, dic2 = {}, {}

        for char in s1:
            dic1[char] = dic1.get(char, 0) + 1
        
        l = 0
        for r, char in enumerate(s2):
            dic2[char] = dic2.get(char, 0) + 1

            if r - l + 1 > len(s1):
                dic2[s2[l]] -= 1
                if dic2[s2[l]] == 0:
                    del dic2[s2[l]]
                l += 1
            
            if dic2 == dic1:
                return True
        
        return False