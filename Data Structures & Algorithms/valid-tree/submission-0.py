from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        edge_map = defaultdict(list)

        for [a, b] in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)
        
        visited = set()

        def dfs(node):

            visited.add(node)
            for nei in edge_map[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)

        return len(visited) == n
