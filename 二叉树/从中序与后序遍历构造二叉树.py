# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def fun(ino,post):
            if len(post)==0:
                return None
            rootvalue=post[len(post)-1]
            root=TreeNode(rootvalue)
            index=0
            for index in range(len(ino)):#这里的切割点可以调用index函数
                if ino[index]==rootvalue:
                    break
            in_left=ino[:index]#切片
            L1=len(in_left)
            in_right=ino[index+1:]
            L2=len(in_right)
          # 切片法划分左右子树
            post_left=post[:L1]
            post_right=post[L1:len(post)-1]
          #对后序数组进行处理
            root.left=fun(in_left,post_left)
            root.right=fun(in_right,post_right)
            return root
        return fun(inorder,postorder)
