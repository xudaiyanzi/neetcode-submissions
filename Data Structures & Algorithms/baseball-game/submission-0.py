class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        indx = 0

        for i, char in enumerate(operations):
            if char == '+':
                val = res[indx - 1] + res[indx - 2]
                res.append(val)
                indx += 1
            elif char == 'C':
                res.pop()
                indx -= 1
            elif char == 'D':
                val = res[indx - 1] * 2
                res.append(val)
                indx += 1
            else:
                val = int(char)
                res.append(val)
                indx += 1
        return sum(res)