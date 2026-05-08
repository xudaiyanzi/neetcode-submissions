class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''
        for char in s:
            if char.isalnum():
                s_clean += char.lower()

        l, r = 0, len(s_clean) - 1

        while l < r:
            if s_clean[l].lower() != s_clean[r].lower():
                return False
            l += 1
            r -= 1
        
        return True