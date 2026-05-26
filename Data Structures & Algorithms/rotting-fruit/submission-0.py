from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n  = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [
            (1, 0), 
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        time = 0
        while q and fresh > 0:
            size = len(q)
            
            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    newr, newc = r + dr, c + dc
                    if newr < 0 or newr >= m or newc < 0 or newc >= n or grid[newr][newc] != 1:
                        continue
                    grid[newr][newc] = 2
                    fresh -= 1

                    q.append((newr, newc)) 

            time += 1
        
        return time if fresh == 0 else -1
                    
