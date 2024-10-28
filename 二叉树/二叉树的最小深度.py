class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def getMin(node):
            if node==None:
                return 0
            if node!=None and node.left==None and node.right==None:
                return 1
            left_height=getMin(node.left)
            right_height=getMin(node.right)
            if node.left==None and node.right!=None:
                return 1+right_height
            elif node.left!=None and node.right==None:
                return 1+left_height
            else:
                return 1+min(left_height,right_height)
        return getMin(root)
