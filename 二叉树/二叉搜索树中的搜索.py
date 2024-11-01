# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node,target):
            if node==None:
                return None
            if node.val==target:
                return node
            #遍历到的节点
            result=None
            if node.val>target:
                result=search(node.left,target)
            if node.val<target:
                result=search(node.right,target)
            return result
        return search(root,val)
