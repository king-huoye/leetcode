# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_length=-1
        self.result=None
        def fun(node,depth):
            if not node:
                return 0
            if not node.left and not node.right:
                if depth>self.max_length:
                    self.max_length=depth
                    self.result=node.val
            if node.left:
                depth+=1
                fun(node.left,depth)
                depth-=1
            if node.right:
                depth+=1
                fun(node.right,depth)
                depth-=1
        fun(root,0)
        return self.result


        
