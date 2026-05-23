# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for (idx, val) in enumerate(inorder)}
        self.preorder_idx = 0

        def helper(left, right):
            if left > right:
                return None
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            root_idx_inorder = inorder_map[root_val]

            self.preorder_idx += 1

            root.left = helper(left, root_idx_inorder - 1)
            root.right = helper(root_idx_inorder + 1, right)
            return root
        
        return helper(0, len(inorder) - 1)