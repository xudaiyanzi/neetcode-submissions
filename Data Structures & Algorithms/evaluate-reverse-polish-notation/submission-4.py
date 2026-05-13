class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        n = len(tokens) 

        if n == 1 and tokens[0] not in operators:
            return int(tokens[0])
        if n == 2:
            return -1
        for i in range(n):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                val = 0
                if tokens[i] == '+':
                    val = val2 + val1
                elif tokens[i] == '-':
                    val = val2 - val1
                elif tokens[i] == '*':
                    val = val2 * val1
                elif tokens[i] == '/':
                    val = int(val2 / val1)
                stack.append(val)
        return stack[-1]

