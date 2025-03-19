# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder,inorder):
            #preorder是前序
            #inorder是中序
            if len(preorder)==0:
                return None
            key=preorder[0]
            root=TreeNode(key)
            Index=inorder.index(key)#找到根节点在中序的位置
            inorder_left=inorder[:Index]
            inorder_right=inorder[Index+1:]
            preorder_left=preorder[1:1+len(inorder_left)]
            preorder_right=preorder[1+len(inorder_left):]
            root.left=construct(preorder_left,inorder_left)
            root.right=construct(preorder_right,inorder_right)
            return root
        return construct(preorder,inorder)
