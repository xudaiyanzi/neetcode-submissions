class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        pre2, pre1 = 0, 0

        for i in range(2, n + 1):
            curr = min(pre2 + cost[i - 2], pre1 + cost[i - 1])
            pre2 = pre1
            pre1 = curr
        
        return pre1