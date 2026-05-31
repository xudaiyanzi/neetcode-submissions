class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        res = []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1]
        ]

        ## dfs
        def dfs(r, c, curr_set):
            curr_set.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if nr >= rows or nr < 0 or nc >= cols or nc < 0:
                    continue
                
                if (nr, nc) in curr_set:
                    continue
                
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, curr_set)
        
        ## pacific
        for c in range(cols):
            dfs(0, c, pac)

        for r in range(rows):
            dfs(r, 0, pac)

        ## Atlantic
        for r in range(rows):
            dfs(r, cols - 1, atl)
        for c in range(cols):
            dfs(rows - 1, c, atl)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
