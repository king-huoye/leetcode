# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder,inorder):
            if len(preorder)==0:
                return None
            treeval=preorder[0]
            root=TreeNode(treeval)
            Index=inorder.index(treeval)#找到在中序的位置
            in_left=inorder[:Index]
            in_right=inorder[Index+1:]
            pre_left=preorder[1:1+len(in_left)]
            pre_right=preorder[1+len(in_left):]
            root.left=construct(pre_left,in_left)
            root.right=construct(pre_right,in_right)
            return root
        return construct(preorder,inorder)
