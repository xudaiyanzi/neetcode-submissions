class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        most_freq = 0
        res = 0
        letter_dic = {}

        while r < len(s):
            letter_dic[s[r]] = letter_dic.get(s[r], 0) + 1
            most_freq = max(most_freq, letter_dic[s[r]])

            while r - l + 1 - most_freq > k:
                letter_dic[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res
                
