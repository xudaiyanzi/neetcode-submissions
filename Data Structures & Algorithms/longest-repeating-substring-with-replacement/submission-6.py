class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, max_freq = 0, 0, 0
        res = 0
        letter_list = [0] * 26
        n = len(s)

        while r < n:
            indx = ord(s[r]) - 65
            letter_list[indx] += 1
            max_freq = max(max_freq, letter_list[indx])
            # print("r: ", r, "max_freq is ", max_freq)
            while l < r and r - l + 1 - max_freq > k:
                # print("l moving from: ",  l, "to ", l + 1)
                letter_list[ord(s[l]) - 65] -= 1
                l += 1
            # print(s[l:(r+1)])
            res = max(res, r - l + 1)
            r += 1

        return res
            