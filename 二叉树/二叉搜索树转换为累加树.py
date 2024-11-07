# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre=0 #用于保存前一个的数值
        def add(node):
            if node==None:
                return 
            add(node.right)
            node.val+=self.pre
            self.pre=node.val
            add(node.left)
        add(root)
        return root
