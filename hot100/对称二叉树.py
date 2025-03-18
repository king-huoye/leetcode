# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        def compare(left,right):
            if left==None and right==None:
                return True
            elif left==None and right!=None:
                return False
            elif left!=None and right==None:
                return False
            elif left.val!=right.val:
                return False
            else:
                Le=compare(left.left,right.right)
                Ri=compare(left.right,right.left)
                return Le and Ri
        return compare(root.left,root.right)
