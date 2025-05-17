# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        que=deque()
        if root:
            que.append(root)
        while que:
            L=len(que)
            level=[]
            while L:
                L-=1
                node=que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(level)
        res=[]
        for i in range(len(result)):
            if i%2==0:
                res.append(result[i])
            else:
                res.append(result[i][::-1])
        return res
