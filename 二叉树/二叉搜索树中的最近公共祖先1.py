# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def travel(node,P,Q):
            if node==None:
                return None
            if node.val>P.val and node.val>Q.val:
                Left=travel(node.left,P,Q)
                if Left:
                    return Left 
            if node.val<P.val and node.val<Q.val:
                Right=travel(node.right,P,Q)
                if Right:
                    return Right
            return node
        return travel(root,p,q)
        
