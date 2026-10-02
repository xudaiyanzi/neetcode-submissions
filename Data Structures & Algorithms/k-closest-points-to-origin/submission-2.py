import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for px, py in points:
            dis = (px ** 2 + py ** 2) ** (1/2)

            heapq.heappush(h, (dis ** (-1), [px, py]))

            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for (val, p) in h:
            res.append(p)
        
        return res