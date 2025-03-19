# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que=deque()
        if root:
            que.append(root)
        res=[]

        while que:
            L=len(que)
            for i in range(L):
                node=que.popleft()
                if i==L-1:
                    res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res

        
