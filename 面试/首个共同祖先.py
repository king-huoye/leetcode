# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find(node,p,q):
            if node==None:
                return None
            if node==p or node==q:
                return node
            Left=find(node.left,p,q)
            Right=find(node.right,p,q)
            if Left==None and Right==None:
                return None
            elif Left==None and Right!=None:
                return Right
            elif Left!=None and Right==None:
                return Left
            elif Left!=None and Right!=None:
                return node

        return find(root,p,q)
