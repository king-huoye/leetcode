# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode()
        cur=dummy
        dummy.next=head
        while cur.next!=None and cur.next.next!=None:
            tmp1=cur.next
            tmp2=cur.next.next.next
            cur.next=cur.next.next
            cur.next.next=tmp1
            tmp1.next=tmp2
            cur=cur.next.next
        return dummy.next

