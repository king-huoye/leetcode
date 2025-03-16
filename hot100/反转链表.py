# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pre=None
        cur=head
        while cur!=None:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
            #指针移动  
        return pre #此时cur指向了None   
       
