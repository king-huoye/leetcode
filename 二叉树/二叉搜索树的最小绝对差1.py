# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.result=float('inf')
        self.pre=None
        def fun(node):
            if node==None:
                return 
            left_num=fun(node.left)
            pre=None
            if self.pre:
                self.result=min(self.result,abs(self.pre.val-node.val))
            self.pre=node
            right_num=fun(node.right)
        fun(root)
        return self.result
