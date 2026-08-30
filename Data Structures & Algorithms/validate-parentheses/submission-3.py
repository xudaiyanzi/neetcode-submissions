class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []

        for char in s:
            print(char)
            if char not in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                out = stack.pop()
                if out != mapping[char]:
                    return False

        return len(stack) == 0
