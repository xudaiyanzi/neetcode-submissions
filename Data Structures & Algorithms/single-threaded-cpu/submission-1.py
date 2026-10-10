import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waiting = []
        for i, [eT, pT] in enumerate(tasks):
            heapq.heappush(waiting, (eT, pT, i))
        
        ready = []
        count = 0
        res = []

        while waiting or ready:
            while waiting and waiting[0][0] <= count:
                nxt = heapq.heappop(waiting)
                heapq.heappush(ready, (nxt[1], nxt[2]))
            if not ready:
                count = waiting[0][0]
                continue
            pT, i = heapq.heappop(ready)
            count += pT
            res.append(i)
        
        return res