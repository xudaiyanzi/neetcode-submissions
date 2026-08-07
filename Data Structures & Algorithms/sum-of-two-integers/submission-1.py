class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            na = (a ^ b) & mask
            nb = ((a & b) << 1) & mask
            a, b = na, nb

        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        
