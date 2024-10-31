# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(num):
            if len(num)==0:
                return None
            if len(num)==1:
                return TreeNode(num[0])#访问到叶子节点的时候
            
            Ma=max(num)
            Index=num.index(Ma)
            root=TreeNode(Ma)
            #划分左和右
            
            tree_left=num[:Index] #处理左子树                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            root.left=construct(tree_left)
            
            tree_right=num[Index+1:]
            root.right=construct(tree_right)
            return root
        return construct(nums)
