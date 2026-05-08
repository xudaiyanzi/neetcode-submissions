class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s:
            if char.isalnum():
                s_list.append(char.lower())
        s_clean = ''.join(s_list)

        l, r = 0, len(s_clean) - 1

        while l < r:
            if s_clean[l].lower() != s_clean[r].lower():
                return False
            l += 1
            r -= 1
        
        return True