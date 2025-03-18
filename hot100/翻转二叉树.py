# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            if node==None:
                return None
            node.left,node.right=node.right,node.left
            reverse(node.left)
            reverse(node.right)
            return node
        return reverse(root)
