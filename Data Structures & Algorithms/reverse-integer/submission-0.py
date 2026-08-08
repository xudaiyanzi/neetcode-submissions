class Solution:
    def reverse(self, x: int) -> int:
        max_x = 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10

            if res > (max_x // 10) or (res == max_x // 10 and digit > 7):
                return 0
            res = res * 10 + digit
            x = x // 10
        
        return res * sign