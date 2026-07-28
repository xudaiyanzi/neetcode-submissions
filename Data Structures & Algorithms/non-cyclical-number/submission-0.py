class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        square_sum = 0

        while n != 1 and n not in seen:
            seen.add(n)
            square_sum = 0
            while n > 0:
                digit = n % 10
                n //= 10
                square_sum += digit ** 2
            n = square_sum
        
        return n == 1
            