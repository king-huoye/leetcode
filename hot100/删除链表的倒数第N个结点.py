# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        fast=head
        while fast!=None and n:
            n-=1
            fast=fast.next
        
        dummy=ListNode()
        slow=dummy
        dummy.next=head
        while fast!=None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
