import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        q = [(0, 0)]
        n = len(points)
        total_cost = 0

        while len(visited) < n:
            cost, idx = heapq.heappop(q)

            if idx in visited:
                continue
            
            visited.add(idx)
            xi, yi = points[idx]
            total_cost += cost

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]

                    dis = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(q, (dis, j))
                    
        return total_cost