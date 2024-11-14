"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                if node.children:
                    que.extend(node.children)
            result.append(level)
        return result
