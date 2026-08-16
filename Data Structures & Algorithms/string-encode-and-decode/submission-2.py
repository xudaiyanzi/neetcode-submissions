class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res += str(n) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        slow, fast = 0, 0
        n = len(s)

        while fast < n:
            if s[fast] == "#":
                length = int(s[slow : fast])
                word = s[(fast + 1) : (fast + 1 + length)]
                res.append(word)
                slow, fast = fast + 1 + length, fast + 2 + length
            else:
                fast += 1
        
        return res

