class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_list = [c for c in s if c.isalnum()]
        l, r = 0, len(s_list) - 1

        while l <= r:
            if s_list[l].lower() != s_list[r].lower():
                return False
            l += 1
            r -= 1
        
        return True