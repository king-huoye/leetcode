# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nums=[]
        cur=head
        while cur:
            nums.append(cur.val)
            cur=cur.next
        count=Counter(nums)
        res=[]
        for key,val in count.items():
            if val==1:
                res.append(key)
        dummy=ListNode()
        cur=dummy
        for i in range(len(res)):
            p=ListNode(res[i])
            cur.next=p
            cur=p
        return dummy.next
