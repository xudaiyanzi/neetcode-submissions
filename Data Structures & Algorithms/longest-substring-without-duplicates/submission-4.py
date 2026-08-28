class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l, res, n = 0, 0, len(s)

        for i in range(n):
            if s[i] in dic:
                l = max(dic[s[i]] + 1, l)
            curr = i - l + 1
            res = max(curr, res)
            dic[s[i]] = i
        
        return res