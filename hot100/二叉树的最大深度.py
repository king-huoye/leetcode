# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cal(node):
            if node==None:
                return 0
            Left=cal(node.left)
            Right=cal(node.right)
            return 1+max(Left,Right)
        return cal(root)
