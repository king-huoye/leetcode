# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node==None:
                return 0
            left_high=check(node.left)
            if left_high==-1:
                return -1
            right_high=check(node.right)
            if right_high==-1:
                return -1
            if abs(left_high-right_high)>1:
                return -1
            return 1+max(left_high,right_high)
        if check(root)==-1:
            return False
        else:
            return True
            
        
