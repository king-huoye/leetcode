# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node,p,q):
            if node==None:#如果是空节点,就不需要去查找了根本没有
                return None
            if p==node or q==node:#要找的节点就是根节点
                return node
            Le=search(node.left,p,q)#右子树去寻找p,q
            Ri=search(node.right,p,q)#右子树找p,q
            if Le==None and Ri!=None:
                return Ri
            elif Le!=None and Ri==None:
                return Le
            elif Le==None and Ri==None:
                return None
            elif Le!=None and Ri!=None:
                return node
        return search(root,p,q)
