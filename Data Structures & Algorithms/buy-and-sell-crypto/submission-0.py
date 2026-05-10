class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        lowp = float('inf')

        for p in prices:
            lowp = min(lowp, p)
            maxp = max(maxp, p - lowp)
        return maxp
        