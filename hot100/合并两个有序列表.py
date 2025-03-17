# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        elif list1==None and list2!=None:
            return list2
        elif list1!=None and list2==None:
            return list1
        else:
            res=[]
            cur1=list1
            cur2=list2
            while cur1:
                res.append(cur1.val)
                cur1=cur1.next
            while cur2:
                res.append(cur2.val)
                cur2=cur2.next
            res.sort()
            dummy=ListNode()
            cur=dummy
            n=len(res)
            for i in range(n):
                Now=ListNode(res[i])
                cur.next=Now
                cur=Now
            return dummy.next
