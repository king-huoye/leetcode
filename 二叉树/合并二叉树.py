# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def Merge(tree1,tree2):
            if tree1==None:
                return tree2
            if tree2==None:
                return tree1
            tree1.val=tree1.val+tree2.val
            tree1.left=Merge(tree1.left,tree2.left)
            tree1.right=Merge(tree1.right,tree2.right)
            return tree1
        return Merge(root1,root2)
