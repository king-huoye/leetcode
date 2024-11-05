# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node,val):
            if node==None:
                treenode=TreeNode(val)#遍历的节点为None就是要插入的位置
                return treenode
            if node.val<val:
                node.right=insert(node.right,val)
            if node.val>val:
                node.left=insert(node.left,val)
            return node
        return insert(root,val)
