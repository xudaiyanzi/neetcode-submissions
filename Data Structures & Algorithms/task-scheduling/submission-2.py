import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        dic = {}
        h = []
        
        for t in tasks:
            dic[t] = dic.get(t, 0) + 1

        for k, v in dic.items():
            heapq.heappush(h, -v)

        time = 0
        wait = deque()

        while h or wait:
            time += 1

            if h:
                freq = heapq.heappop(h)
                freq += 1
                if freq != 0:
                    wait.append((freq, n + time))
            if wait and wait[0][1] == time:
                freq, pushtime = wait.popleft()
                heapq.heappush(h, freq)
        return time 


