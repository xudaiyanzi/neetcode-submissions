import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heapq.heappush(h, s * (-1))
        
        while h:
            y = heapq.heappop(h)

            if not h:
                return y * (-1)
            
            x = heapq.heappop(h)

            if y == x:
                continue
            elif y * (-1) > x * (-1):
                heapq.heappush(h, (y - x))
        
        return 0