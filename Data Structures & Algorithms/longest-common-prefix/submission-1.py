class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])

        for i in range(n):
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
                
        return strs[0]

        