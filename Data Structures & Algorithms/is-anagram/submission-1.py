class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        s_dic = {}
        t_dic = {}

        for i in range(n):
            s_dic[s[i]] = s_dic.get(s[i], 0) + 1
            t_dic[t[i]] = t_dic.get(t[i], 0) + 1

        for char, count in s_dic.items():
            if char not in t_dic or t_dic[char] != count:
                return False
        
        return True

        