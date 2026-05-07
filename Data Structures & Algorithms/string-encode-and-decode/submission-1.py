class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '/' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        end = len(s)

        while i < end:
            j = i
            while s[j] != '/':
                j += 1
            length = int(s[i:j]) # it is the number before '/'
            res.append(s[(j + 1): (j + 1 + length)])

            i = j + 1 + length
        return res
