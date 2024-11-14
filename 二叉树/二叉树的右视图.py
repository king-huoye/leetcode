# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        output=[]
        for i in range(len(result)):
            for j in range(len(result[i])):
                if j==len(result[i])-1:
                    output.append(result[i][j]) #取每一层的最后一个即可
        return output

        
