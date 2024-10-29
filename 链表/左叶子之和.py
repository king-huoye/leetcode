class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def co(node):
            if node==None:
                return 0
            if node.left==None and node.right==None:
                return 0
            #左右中
            leftNum=co(node.left)
            if node.left!=None and node.left.left==None and node.left.right==None:
                leftNum=node.left.val #这个逻辑要注意
            rightNum=co(node.right)#也需要判断是否是左叶子节点
        
            all=leftNum+rightNum
            return all
        return co(root)
  #类似求完全二叉树节点的数量,后序遍历，只多了一步判断节点是否为左叶子
