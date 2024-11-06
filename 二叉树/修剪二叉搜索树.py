# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def travel(node,low,high):
            if node==None:
                return None
            if node.val<low:
                right=travel(node.right,low,high)
                return right
            if node.val>high:
                left=travel(node.left,low,high)
                return left
            node.left=travel(node.left,low,high)#处理当前节点
            node.right=travel(node.right,low,high)
            return node
        return travel(root,low,high)
