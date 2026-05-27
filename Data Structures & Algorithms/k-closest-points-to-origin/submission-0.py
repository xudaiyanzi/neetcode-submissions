import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for p in points:
            d = (p[0] ** 2 + p[1] ** 2) ** (1/2)

            heapq.heappush(q, ((-1) * d, p))

            if len(q) > k:
                heapq.heappop(q)
        
        return [items[1] for items in q]
        