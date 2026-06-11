class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        pre2, pre1 = 1, 2

        for _ in range(3, n + 1):
            curr = pre1 + pre2
            pre2 = pre1
            pre1 = curr
        
        return pre1