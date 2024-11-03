# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result=[]
        Min_result=float('inf')
        def zhongxu(node):
            if node==None:
                return 
            zhongxu(node.left)
            result.append(node.val)
            zhongxu(node.right)
        zhongxu(root)
        for i in range(len(result)-1):
            Min_result=min(Min_result,abs(result[i]-result[i+1]))
        return Min_result
