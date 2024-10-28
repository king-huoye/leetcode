# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if node is None:
                return 0  # 空节点的深度为0

            left_height = check_balance(node.left)  # 递归计算左子树高度
            if left_height == -1:  # 左子树不平衡
                return -1
            
            right_height = check_balance(node.right)  # 递归计算右子树高度
            if right_height == -1:  # 右子树不平衡
                return -1
            
            if abs(left_height - right_height) > 1:  # 当前节点不平衡
                return -1
            
            return max(left_height, right_height) + 1  # 返回当前节点的高度

        return check_balance(root) != -1  # 如果返回值不为-1，则树是平衡的
#参数：当前传入节点。 返回值：以当前传入节点为根节点的树的高度。
#修改后的代码在同一个递归过程中计算高度并判断平衡。当发现某个子树的高度差超过 1 时，立刻返回 -1，指示不平衡。这种方式避免了后续不必要的计算。
