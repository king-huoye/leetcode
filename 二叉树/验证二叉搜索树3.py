# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre=None #记录前一个节点
        if root==None:
            return True
        def fun(node):
            if node==None:
                return True
            Is_left=fun(node.left)
            if self.pre!=None and self.pre.val>=node.val:
                return False
            self.pre=node #pre相当于前驱节点
            Is_right=fun(node.right)
            return Is_left and Is_right
        return fun(root)
