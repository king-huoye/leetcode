# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        cur1=headA
        cur2=headB
        lena=0
        lenb=0
        while cur1:
            cur1=cur1.next
            lena+=1
        while cur2:
            cur2=cur2.next
            lenb+=1
        cura=headA
        curb=headB
        if lena>lenb:
            cura,curb=curb,cura
            lena,lenb=lenb,lena
        for i in range(lenb-lena):#相当于快指针先走
            curb=curb.next
        while cura:
            if cura==curb:
                return cura
            else:
                cura=cura.next
                curb=curb.next
        return None
