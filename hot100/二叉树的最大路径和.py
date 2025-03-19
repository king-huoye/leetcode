# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float('-inf')
        def findMax(node):#递归计算以当前节点为起点的 最大贡献值。
            if node==None:
                return 0
            left_sum=max(findMax(node.left),0) #选择 0，表示不走该子树
            right_sum=max(findMax(node.right),0)
            cur_sum=node.val+left_sum+right_sum
            self.maxsum=max(self.maxsum,cur_sum)
            return node.val+max(left_sum,right_sum) #返回最大贡献值
        findMax(root)
        return self.maxsum
