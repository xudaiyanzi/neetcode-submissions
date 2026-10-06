import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}

        for t in tasks:
            dic[t] = dic.get(t, 0) - 1
        
        h = []
        for char, count in dic.items():
            heapq.heappush(h, count)
        
        cyc = 0
        q = deque()
        while h or q:
            cyc += 1
            if not h:
                cyc = q[0][1]
            else:
                count = heapq.heappop(h) + 1
                if count:
                    q.append([count, cyc + n])
            
            if q and q[0][1] == cyc:
                heapq.heappush(h, q.popleft()[0])
        return cyc