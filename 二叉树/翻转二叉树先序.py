# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def Inver(root):
            if root==None:
                return []
            
            Inver(root.left)
            Inver(root.right)
            root.left,root.right=root.right,root.left
        Inver(root)
        return root   
