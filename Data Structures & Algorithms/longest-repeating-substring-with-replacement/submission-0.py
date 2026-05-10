class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dic = {}
        l = 0
        longest, max_freq = 0, 0
        
        for r, char in enumerate(s):
            char_dic[char] = char_dic.get(char, 0) + 1
            max_freq = max(max_freq, char_dic[char])

            while (r - l + 1) - max_freq > k:
                char_dic[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            
        return longest