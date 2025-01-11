# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode()
        seen=set()
        tail=dummy
        cur=head
        while cur:
            if cur.val not in seen:
                seen.add(cur.val)#集合存储保存过的元素,这样不会破坏相对位置关系
                tail.next=ListNode(cur.val)
                tail=tail.next
            cur=cur.next
        return dummy.next
