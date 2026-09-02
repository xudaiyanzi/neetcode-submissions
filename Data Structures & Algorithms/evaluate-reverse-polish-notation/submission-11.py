class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operators = ['+', '-', '*', '/']

        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                out1 = stack.pop()
                out2 = stack.pop()
                # print('out1: ', out1, 'out2: ', out2)
                if char == '+':
                    res = out2 + out1
                elif char == '-':
                    res = out2 - out1
                elif char == '*':
                    res = out2 * out1
                elif char == '/':
                    res = int(out2 / out1)
                # print('char is', char, ', and res is', res)
                stack.append(res)
            
        return stack[-1]