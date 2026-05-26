class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        def dfs(r, c, steps):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            elif grid[r][c] == -1:
                return
            elif steps > grid[r][c]:
                return
            else:
                grid[r][c] = steps
                dfs(r - 1, c, steps + 1)
                dfs(r + 1, c, steps + 1)
                dfs(r, c - 1, steps + 1)
                dfs(r, c + 1, steps + 1)
            return

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == -1:
                    continue
                if grid[r][c] == 0:
                    dfs(r, c, 0)     
        return
