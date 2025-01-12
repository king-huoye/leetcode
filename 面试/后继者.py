# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        result=[]
        def inorder(node):
            if node==None:
                return None
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        value=p.val
        if value not in result:
            return None
        else:
            Index=result.index(value)#获取索引坐标
            if Index==len(result)-1:
                return None #最后一个节点找不到后继
            else:
                return TreeNode(result[Index+1])
