# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.small = []
        self.res = -1

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            self.small.append(node.val)
            if len(self.small) == k:
                self.res = self.small[k - 1]
                return
            
            dfs(node.right)

            return
        dfs(root)
        return self.res