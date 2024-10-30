# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def co(node):
            if node==None:
                return 0
            if node.left==None and node.right==None:#特殊情况
                return 0
            #左右中
            leftNum=co(node.left)
            if node.left!=None and node.left.left==None and node.left.right==None:#这个是左叶子的判断逻辑
                leftNum=node.left.val #这个逻辑要注意
            rightNum=co(node.right)#也需要判断是否是左叶子节点
        
            all=leftNum+rightNum
            return all
        return co(root)
