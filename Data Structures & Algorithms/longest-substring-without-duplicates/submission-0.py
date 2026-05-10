class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        seen_dic = {}
        longest = 1
        l = 0

        for r, char in enumerate(s):
            if char in seen_dic:
                l = max(seen_dic[char] + 1, l)
            seen_dic[char] = r
            longest = max(longest, r - l + 1)
        return longest

        