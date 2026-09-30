# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {val: index for index, val in enumerate(inorder)}
        self.pointer = 0

        def build(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.pointer])
            self.pointer += 1
            inorder_index = dic[root.val]
            root.left = build(l, inorder_index - 1)
            root.right = build(inorder_index + 1, r)
            return root
        
        return build(0, len(inorder) - 1)
