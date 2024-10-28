class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if root==None:
            return []
        que=deque()
        if root:
            que.append(root)
        while que:
            L=len(que)
            level=[]#用来保存每一层的结果
            while L:
                L-=1
                node=que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(level)
        return result
        
