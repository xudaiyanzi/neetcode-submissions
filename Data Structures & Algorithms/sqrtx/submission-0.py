class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            mid = (l + r) // 2
            curr = mid * mid
            print(l, r)

            if curr > x:
                r = mid - 1
            elif curr < x:
                l = mid + 1
            else:
                return mid
        
        return l - 1