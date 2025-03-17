# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        res=[]
        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        #存好数组
        for i in range(0,len(res),k):
            if i+k>len(res):
                break
            res[:]=res[:i]+res[i:i+k][::-1]+res[i+k:]
        dummy=ListNode()
        now=dummy
        for i in range(len(res)):
            tmp=ListNode(res[i])
            now.next=tmp
            now=tmp
        return dummy.next
