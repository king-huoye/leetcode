# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node,key):
            if node==None:
                return None
            if node.val==key:
                if node.left==None and node.right==None: #刚好删除到叶子节点
                    return None
                elif node.left!=None and node.right==None:
                    return node.left #左孩子补位
                elif node.right!=None and node.left==None:
                    return node.right #右孩子补位
                else:
                    cur=node.right
                    while cur.left:
                        cur=cur.left
                    cur.left=node.left #删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上/
                    return node.right
            if key<node.val:
                node.left=delete(node.left,key) #往左子树去寻找
            if key>node.val:
                node.right=delete(node.right,key) #往右子树去寻找
            return node
        return delete(root,key)
