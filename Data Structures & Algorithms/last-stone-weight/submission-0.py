import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []

        for s in stones:
            heapq.heappush(q, -1 * s)
        
        while len(q) > 1:
            w1 = heapq.heappop(q)
            w2 = heapq.heappop(q)

            w1 = -1 * w1
            w2 = -1 * w2

            if w1 != w2:
                d = abs(w1 - w2)
                heapq.heappush(q, -1 * d)
        
        return q[0] * (-1) if q else 0
