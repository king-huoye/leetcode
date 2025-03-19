# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #回溯
        def dfs(node,targetSum):
            if node==None:
                return 0
            res=0
            if node.val==targetSum:
                res+=1
            res+=dfs(node.left,targetSum-node.val)
            res+=dfs(node.right,targetSum-node.val)
            return res
        if root==None:
            return 0
        res=dfs(root,targetSum)#对当前节点处理
        res+=self.pathSum(root.left,targetSum)#整棵树
        res+=self.pathSum(root.right,targetSum)
        return res

