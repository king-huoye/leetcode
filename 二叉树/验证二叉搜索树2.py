# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        self.maxvalue=float('-inf') #设定极小值进行比较
        def fun(node):
            if node==None:
                return True
            Is_left=fun(node.left)
            if node.val>self.maxvalue:#这个是根据定义去判断
                self.maxvalue=node.val
            else:
                return False
            Is_right=fun(node.right)
            return Is_left and Is_right
        return fun(root)
