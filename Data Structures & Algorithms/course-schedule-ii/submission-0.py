from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, visiting = set(), set()
        pre_map = defaultdict(list)
        res = []

        for [a, b] in prerequisites:
            pre_map[a].append(b)

        def dfs(c):
            if c in visited:
                return True
            
            if c in visiting:
                return False
            
            visiting.add(c)
            for pre in pre_map[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

