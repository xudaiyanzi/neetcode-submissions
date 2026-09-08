class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        word = ''

        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char == '[':
                stack.append((word, num))
                word = ''
                num = 0
            elif char != ']':
                word += char
            elif char == ']':
                curr_word, curr_num = stack.pop()
                word = curr_word + curr_num * word
        
        return word


