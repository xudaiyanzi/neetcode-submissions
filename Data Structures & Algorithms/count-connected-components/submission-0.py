from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_map = defaultdict(list)
        res = 0
        visited = set()

        for a, b in edges:
            edges_map[a].append(b)
            edges_map[b].append(a)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in edges_map[node]:
                dfs(nei)
            return
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res
            

