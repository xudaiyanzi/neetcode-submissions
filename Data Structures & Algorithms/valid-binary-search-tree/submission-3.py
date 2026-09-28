# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True

            if node.left and node.left.val >= node.val:
                return False
            
            if node.right and node.right.val <= node.val:
                return False
            
            if node.val >= large or node.val <= small:
                return False
             
            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)

            return left and right

        return dfs(root, -float('inf'), float('inf'))