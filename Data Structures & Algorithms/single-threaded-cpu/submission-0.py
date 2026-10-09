import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        res = []

        for i, [enqueueTime, processTime] in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processTime, i))
        
        available_time = 0
        available = []
        while pending or available:
            while pending and pending[0][0] <= available_time:
                enqueueTime, processingTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processingTime, i))
            if not available:
                available_time = pending[0][0]
                continue
            processingTime, i = heapq.heappop(available)
            available_time += processingTime
            res.append(i)
        
        return res
            

            


