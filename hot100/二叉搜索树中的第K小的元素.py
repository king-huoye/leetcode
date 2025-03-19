# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def fun(node):
            if node==None:
                return 
            fun(node.left)
            res.append(node.val)
            fun(node.right)
        fun(root)
        if k>len(res):
            return -1
        return res[k-1]
        
