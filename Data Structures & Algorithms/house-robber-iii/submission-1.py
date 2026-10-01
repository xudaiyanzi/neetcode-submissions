# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dic = {None: 0}
        def dfs(node):
            if not node:
                return 0
            if node in dic:
                return dic[node]

            res = node.val

            if node.left:
                res += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                res += dfs(node.right.left) + dfs(node.right.right)
            
            skip = dfs(node.left) + dfs(node.right)
            best = max(res, skip)
            dic[node] = best

            return best
        return dfs(root)