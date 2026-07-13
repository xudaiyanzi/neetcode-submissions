class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}

        for i in range(len(s)):
            seen[s[i]] = i

        res, p, pre_p = [], 0, -1

        for i in range(len(s)):
            last_char_pos = seen[s[i]]
            p = max(p, last_char_pos)
            if p == i:
                res.append(p - pre_p)
                pre_p = p
        
        return res
