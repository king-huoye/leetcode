class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        re=[]
        def res(node):
            if node==None:
                return None
            re.append(node.val)
            res(node.left)
            res(node.right)
        res(root) #不断调用递归函数
        return re
