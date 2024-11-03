# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums=[]
        if root==None:
            return True
        def fun(node):
            if node==None:
                return 
            fun(node.left)
            nums.append(node.val)
            fun(node.right)
        fun(root)
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                return False
        return True
