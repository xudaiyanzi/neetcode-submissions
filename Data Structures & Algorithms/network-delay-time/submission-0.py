from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect_map = defaultdict(list)

        for s, t, w in times:
            connect_map[s].append([w, t])
        
        q = []
        q.append((0, k))
        visited = set()
        total_w = 0

        while q:
            w, t = heapq.heappop(q)
            if t in visited:
                continue
            
            visited.add(t)
            total_w = w

            for nei_w, nei_node in connect_map[t]:
                heapq.heappush(q, (nei_w + w, nei_node))
        
        return total_w if len(visited) == n else -1
        
