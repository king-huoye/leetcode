# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def fun(node):
            if node==None:
                return 
            fun(node.left)
            result.append(node.val)
            fun(node.right)
        fun(root)
        return result
