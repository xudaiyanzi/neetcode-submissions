class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        n = len(digits)
        digi_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def backtrack(path, i):
            if i == n:
                s = ''.join(path)
                res.append(s)
                return

            curr = digits[i]
            candidates = digi_map[curr]
            for c in candidates:
                path.append(c)
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return res