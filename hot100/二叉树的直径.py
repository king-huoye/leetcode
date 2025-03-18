# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ds=0
        def calculate(node):
            if node==None:
                return 0
            left_height=calculate(node.left)
            right_height=calculate(node.right)
            self.ds=max(self.ds,left_height+right_height)#算边数
            return max(left_height,right_height)+1
        calculate(root)
        return self.ds
