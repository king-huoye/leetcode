# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        if left==right:
            return head
        left_index=left-1
        right_index=right-1
        nums=[]
        cur=head
        while cur:
            nums.append(cur.val)
            cur=cur.next
        nums[:]=nums[:left_index]+nums[left_index:right][::-1]+nums[right:]
        dummy=ListNode()
        cur=dummy
        for i in range(len(nums)):
            p=ListNode(nums[i])
            cur.next=p 
            cur=p
        return dummy.next
