class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        for char in s:
            if char in char_map:
                if not stack or len(stack) == 0:
                    return False
                    
                if stack[-1] == char_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0