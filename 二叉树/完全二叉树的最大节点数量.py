# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        que=deque()
        result=[]
        if root:
            que.append(root)
        while que:
            L=len(que)
            while L:
                L-=1
                node=que.popleft()
                result.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return len(result)   
