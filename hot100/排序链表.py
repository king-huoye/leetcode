# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        res=[]
        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        res.sort()
        dummy=ListNode()
        cu=dummy
        for num in res:
            tmp=ListNode(num)
            cu.next=tmp 
            cu=tmp
        return dummy.next
