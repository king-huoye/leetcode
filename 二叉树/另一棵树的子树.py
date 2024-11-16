class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        # 定义判断两棵树是否相同的函数
        def judge(P, Q):
            if P is None and Q is None:
                return True
            if P is None or Q is None or P.val != Q.val:
                return False
            return judge(P.left, Q.left) and judge(P.right, Q.right)
        
        # 判断当前节点是否匹配
        return judge(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
