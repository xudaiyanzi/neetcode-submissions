class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_l, best_r = 0, 0
        n = len(s)

        def expand(l, r):
            
            while l >= 0 and r < n and s[l] == s[r]: 
                l -= 1
                r += 1
            
            return l + 1, r - 1

        if n <= 1:
            return s

        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        for i in range(1, n):
            l1, r1 = expand(i - 1, i)
            l2, r2 = expand(i - 1, i + 1)
            if r1 - l1 >= r2 - l2 and r1 - l1 >= best_r - best_l:
                best_l, best_r = l1, r1
            elif r2 - l2 >= r1 - l1 and r2 - l2 >= best_r - best_l:
                best_l, best_r = l2, r2
        return s[best_l: best_r + 1]
                

        
        