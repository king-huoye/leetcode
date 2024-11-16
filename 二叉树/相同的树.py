# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q!=None:
            return False
        if p!=None and q==None:
            return False
        if p==None and q==None:
            return True
        def judge(P,Q):
            if P==None and Q==None:
                return True
            if P==None and Q!=None:
                return False
            if P!=None and Q==None:
                return False
            if P.val!=Q.val:
                return False
            Left=judge(P.left,Q.left)
            Right=judge(P.right,Q.right)
            return Left and Right
        return judge(p,q)
        
