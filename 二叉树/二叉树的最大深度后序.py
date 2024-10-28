class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(node):
            if node==None:
                return 0
            left_depth=getDepth(node.left)
            right_depth=getDepth(node.right)
            Ma=1+max(left_depth,right_depth)#中间处理过程,后序遍历
            return Ma
        return getDepth(root)
