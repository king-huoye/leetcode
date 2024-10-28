class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        def compare(left,right):
            if left==None and right!=None:
                return False
            elif left!=None and right==None:
                return False
            elif left==None and right==None:
                return True
            elif left.val!=right.val:
                return False
            outside=compare(left.left,right.right)
            inside=compare(left.right,right.left)
            result=outside and inside
            return result
        return compare(root.left,root.right)
