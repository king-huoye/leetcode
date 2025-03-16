# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena=0
        lenb=0
        cura=headA
        curb=headB
        while cura:
            lena+=1
            cura=cura.next
        #计算链表长度
        while curb:
            lenb+=1
            curb=curb.next
        cura=headA
        curb=headB
        #重新指定指针
        if lena>lenb:
            lena,lenb=lenb,lena
            cura,curb=curb,cura
        #长度的提前先走
        for i in range(lenb-lena):
            curb=curb.next
        while cura:
            if cura==curb:
                return cura
            else:
                cura=cura.next
                curb=curb.next
        return None

        
