# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def cou(node):
            if node==None:
                return 0
            left_num=cou(node.left)#计算左子树
            right_num=cou(node.right)#计算右子树
            all=1+left_num+right_num#根节点的
            return all
        return cou(root)
