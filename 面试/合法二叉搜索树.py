# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result=[]
        def inorder(node):
            if node==None:
                return None
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        if root==None:
            return True
        inorder(root)
        for i in range(len(result)-1):
            if result[i+1]-result[i]<=0:
                return False
        return True
