class Solution:
    def simplifyPath(self, path: str) -> str:
        clean_path = path.split('/')
        stack = []

        for word in clean_path:
            if not word or word == '.':
                continue
            elif word == '..':
                if stack:
                    out = stack.pop()
            else:
                stack.append(word)
        
        return '/' + '/'.join(stack)