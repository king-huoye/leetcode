# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        que=deque()
        if tree:
            que.append(tree)
        result=[]
        while que:
            L=len(que)
            dummy=ListNode(0)
            cur=dummy
            while L:
                L-=1
                node=que.popleft()
                cur.next=ListNode(node.val)
                cur=cur.next
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(dummy.next)#把虚拟头节点的next所有加进去
        return result
