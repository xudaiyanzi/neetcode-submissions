from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)

        for [a, b] in prerequisites:
            pre_map[b].append(a)
        
        visited = set()
        visiting = set()

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

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True