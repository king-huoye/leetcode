# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def fun(node,count):
            if node==None:
                return False
            
            if node.left==None and node.right==None and count==0:#用于判断只有一个节点的时候,所以传进来的值需要对target减去根节点的值
                return True 
            
            if node.left:
                count=count-node.left.val
                if fun(node.left,count):
                    return True
                count=count+node.left.val #回溯法
            if node.right:
                count=count-node.right.val
                if fun(node.right,count):
                    return True
                count=count+node.right.val
            return False
        if root==None:
            return False
        return fun(root,targetSum-root.val)
        
