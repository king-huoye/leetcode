# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n=len(lists) #长度
        res=[]
        for lst in lists:#直接遍历链表数组
            while lst:
                res.append(lst.val)
                lst=lst.next
        res.sort()
        dummy=ListNode()
        cur=dummy
        for i in range(len(res)):
            tmp=ListNode(res[i])
            cur.next=tmp
            cur=tmp
        return dummy.next
        
