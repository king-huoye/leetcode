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
            if node==P or node==Q:
                return node #所遍历的节点就是对应的公共祖先节点
            Left_=travel(node.left,P,Q)
            Right_=travel(node.right,P,Q)
            #中间判断
            if Left_ and Right_: #左子树出现节点p，右子树出现q,或者左出现q或者右出现p
                return node
            elif not Left_ and not Right_:
                return None
            elif Left_ and not Right_:
                return Left_
            elif not Left_ and Right_:
                return Right_
        return travel(root,p,q)
        
