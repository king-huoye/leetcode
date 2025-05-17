# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #先序遍历
        self.result=[]
        self.path=[]
        def preorder(root):
            if root==None:
                return 
            self.path.append(str(root.val))
            if root.left==None and root.right==None:
                self.result.append(''.join(self.path[:]))
                #收集结果
            else:
                preorder(root.left)
                preorder(root.right)
            self.path.pop()
        if not root:
            return 0
        preorder(root)
        res=0
        for char in self.result:
            res+=int(char)
        return res
