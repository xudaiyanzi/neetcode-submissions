class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        s1_dic, window_dic = {}, {}

        for char in s1:
            s1_dic[char] = s1_dic.get(char, 0) + 1
        for char in s2[:n1]:
            window_dic[char] = window_dic.get(char, 0) + 1
        
        if s1_dic == window_dic:
            return True

        for r in range(n1, n2):
            new_char = s2[r]
            window_dic[new_char] = window_dic.get(new_char, 0) + 1
            l = r - n1
            rm_char = s2[l]
            window_dic[rm_char] -= 1
            if window_dic[rm_char] == 0:
                del window_dic[rm_char]
            if window_dic == s1_dic:
                return True
        
        return False



