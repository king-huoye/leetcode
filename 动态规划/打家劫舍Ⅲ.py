# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def fun(node):
            if not node:
                return [0,0]
            left=fun(node.left)
            right=fun(node.right)

            ro=node.val+left[1]+right[1]
            not_rob=max(left)+max(right)#不偷当前节点,左右最大
            return [ro,not_rob]
        return max(fun(root))
        
