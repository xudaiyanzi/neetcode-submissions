class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        
        def union(a, b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return False
            
            elif pa > pb:
                par[pa] = pb
            else:
                par[pb] = pa
            return True
        
        for [a, b] in edges:
            if not union(a, b):
                return [a, b]
