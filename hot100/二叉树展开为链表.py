# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res=[]
        def fun(node):
            if node==None:
                return 
            res.append(node)#存放结点
            fun(node.left)
            fun(node.right)
        fun(root)
        for i in range(1,len(res)):
            pre,cur=res[i-1],res[i]
            pre.left=None
            pre.right=cur
