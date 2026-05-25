"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copy_map = {}

        def dfs(curr):
            if curr in copy_map:
                return copy_map[curr]
            
            cp = Node(curr.val)
            copy_map[curr] = cp

            for neighbor in curr.neighbors:
                cp.neighbors.append(dfs(neighbor))
            
            return cp
        
        return dfs(node)


